from django.urls import path
from .views import AddBookView, ListBooksView, BorrowBookView, ReturnBookView, BorrowedBooksView, BorrowingHistoryView

urlpatterns = [
    path("books/", AddBookView.as_view(), name="add_book"), # to post a new book
    path("books/list/", ListBooksView.as_view(), name="list_books"), # to list out the books
    path("borrow/", BorrowBookView.as_view(), name="borrow_book"), # to borrow a book
    path("return/", ReturnBookView.as_view(), name="return_book"), # to return a book
    path("borrowed/<int:borrower_id>/", BorrowedBooksView.as_view(), name="borrowed_books"), # to see the book borrwoed and not returned by a user 
    path("history/<int:borrower_id>/", BorrowingHistoryView.as_view(), name="borrowing_history"), # to see the entire borrow history of a user
]
