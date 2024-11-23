from django.db import models
import datetime
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    total_count = models.PositiveIntegerField(default=1) 
    borrow_count = models.PositiveIntegerField(default=0) 
    available = models.BooleanField(default=True) 

    def save(self, *args, **kwargs):
        self.available = self.borrow_count < self.total_count
        super().save(*args, **kwargs)

class Borrower(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def check_activity(self):
        last_loan = Loan.objects.filter(borrower=self).order_by('-borrow_date').first()
        if last_loan and last_loan.borrow_date < (timezone.now() - datetime.timedelta(days=30 * 6)):
            self.is_active = False
            self.save()

    def __str__(self):
        return self.name

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.borrower} borrowed {self.book}"
