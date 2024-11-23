**Library Management System**
A Django-based RESTful application to manage books, borrowers, and loans. This project allows users to manage books, handle borrowing and returning, and track borrower history efficiently.
**Project Overview**
This system provides:
Book management: Add and list books with availability filters.
Borrowing and returning books with membership rules.
Borrower activity validation and borrowing limit enforcement.
APIs for listing borrowed books and viewing borrowing history.

**Base URL**:

http://127.0.0.1:8000/

**Endpoints**:

1. Book Management
   
**Add Book (http://127.0.0.1:8000/api/books/):** Add a new book to the books table.

![Screenshot 2024-11-23 181152](https://github.com/user-attachments/assets/ed36f8cf-a2be-433e-95bc-e9ee48206334)

**List Book (http://127.0.0.1:8000/api/books/list/):** Lists out all Books:

![Screenshot 2024-11-23 182028](https://github.com/user-attachments/assets/5529dd6f-0b8c-4f1a-a952-407b435804e4)

**List with available tag (http://127.0.0.1:8000/api/books/list/?available=true ):** Lists out available books

![Screenshot 2024-11-23 182056](https://github.com/user-attachments/assets/eae51991-700b-4d84-a38d-6fdc811038ce)

**Borrow a Book (http://127.0.0.1:8000/api/borrow/):** Borrowing a book by passing book_id and borrower_id if borrower already there ,if borrower is not there then the details of the borrower has to be passed. 

![Screenshot 2024-11-23 181603](https://github.com/user-attachments/assets/6bc15b71-5a3d-4472-8968-ffbe30f71a50)

![Screenshot 2024-11-23 181730](https://github.com/user-attachments/assets/c0780387-7fae-4976-8139-2ee5a1e8c8f4)

**Return a Book (http://127.0.0.1:8000/api/return/):** returning the book by particular user by passing the book_id and borrower_id

![Screenshot 2024-11-23 182640](https://github.com/user-attachments/assets/dfc38b19-0e25-43bf-9c46-44247427a890)

**Borrower Data (http://127.0.0.1:8000/api/borrowed/<borrower_id>):** Provides the books that are borrowed by particular user

![Screenshot 2024-11-23 183357](https://github.com/user-attachments/assets/90293773-9ec3-4231-8914-83e1d1172891)

**View Borrowing History (http://127.0.0.1:8000/api/history/<borrower_id>):** Return the entire borrowing history of the user

![Screenshot 2024-11-23 183714](https://github.com/user-attachments/assets/0fdf474c-45ab-4bc3-8ddc-066b3965dc77)
