from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Borrower, Loan
from django.shortcuts import get_object_or_404

class AddBookView(APIView):
    def post(self, request):
        title = request.data.get("title")
        author = request.data.get("author")
        total_count=request.data.get("total_count")
        b=Book.objects.filter(title=title,author=author)
        if b:
            return Response({"message":"Book already posted"})
        book = Book.objects.create(title=title, author=author,total_count=total_count)
        return Response({"message": "Book added", "book_id": book.id}, status=status.HTTP_201_CREATED)

class ListBooksView(APIView):
    def get(self, request):
        available = request.query_params.get("available")
        if available is not None:
            books = Book.objects.filter(available=(available.lower() == "true"))
        else:
            books = Book.objects.all()
        books_data = [{"id": book.id, "title": book.title, "author": book.author, "available": book.available} for book in books]
        return Response(books_data)


class BorrowBookView(APIView):
    def post(self, request):
        book_id = request.data.get("book_id")
        borrower_id = request.data.get("borrower_id")
        borrower_data = request.data.get("borrower_data")
        
        book = get_object_or_404(Book, id=book_id)
        if not book.available:
            return Response({"error": "Book is unavailable or already loaned out."}, status=status.HTTP_400_BAD_REQUEST)

        
        if borrower_id:
            borrower = get_object_or_404(Borrower, id=borrower_id)
            borrower.check_activity()
        elif borrower_data:
            try:
                borrower = Borrower.objects.create(
                    name=borrower_data["name"],
                    email=borrower_data["email"],
                    is_active=borrower_data.get("is_active", True) 
                )
            except Exception as e:
                return Response({"error": f"Failed to create borrower: {str(e)}"})
        else:
            return Response({"error": "Borrower information is required."}, status=status.HTTP_400_BAD_REQUEST)

        if not borrower.is_active:
            return Response({"error": "Borrower membership is inactive."}, status=status.HTTP_403_FORBIDDEN)

        active_loans = Loan.objects.filter(borrower=borrower, is_returned=False).count()
        if active_loans >= 3:
            return Response({"error": "Borrowing limit reached (3 active books)."}, status=status.HTTP_403_FORBIDDEN)

        if not Loan.objects.filter(borrower_id=borrower.id,book_id=book.id):
            Loan.objects.create(book=book, borrower=borrower)
        else:
            return Response({"error": "Borrower already borrowed this book."}, status=status.HTTP_403_FORBIDDEN)
        book.borrow_count += 1 
        book.available = book.borrow_count < book.total_count
        book.save()

        return Response(
            {"message": f"Book '{book.title}' borrowed by '{borrower.name}'", "borrower_id": borrower.id},
            status=status.HTTP_200_OK
        )

import datetime
class ReturnBookView(APIView):
    def post(self, request):
        book_id = request.data.get("book_id")
        borrower_id = request.data.get("borrower_id")
        loan = get_object_or_404(Loan, book_id=book_id,borrower_id=borrower_id, is_returned=False)

        loan.is_returned = True
        loan.return_date = datetime.datetime.now()
        loan.save()

        book = loan.book
        book.borrow_count-=1
        book.available=True
        book.save()

        return Response({"message": f"{book.title} returned"}, status=status.HTTP_200_OK)

class BorrowedBooksView(APIView):
    def get(self, request, borrower_id):
        loans = Loan.objects.filter(borrower_id=borrower_id, is_returned=False)
        books_data = [{"id": loan.book.id, "title": loan.book.title, "author": loan.book.author} for loan in loans]
        return Response(books_data)
        
class BorrowingHistoryView(APIView):
    def get(self, request, borrower_id):
        loans = Loan.objects.filter(borrower_id=borrower_id)
        history = [
            {
                "id": loan.book.id,
                "title": loan.book.title,
                "author": loan.book.author,
                "borrow_date": loan.borrow_date,
                "return_date": loan.return_date,
                "is_returned": loan.is_returned,
            }
            for loan in loans
        ]
        return Response(history)