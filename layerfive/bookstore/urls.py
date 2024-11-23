from django.urls import path
from .views import AddBookView, ListBooksView, BorrowBookView, ReturnBookView, BorrowedBooksView, BorrowingHistoryView

urlpatterns = [
    path("books/", AddBookView.as_view(), name="add_book"),
    path("books/list/", ListBooksView.as_view(), name="list_books"),
    path("borrow/", BorrowBookView.as_view(), name="borrow_book"),
    path("return/", ReturnBookView.as_view(), name="return_book"),
    path("borrowed/<int:borrower_id>/", BorrowedBooksView.as_view(), name="borrowed_books"),
    path("history/<int:borrower_id>/", BorrowingHistoryView.as_view(), name="borrowing_history"),
]
