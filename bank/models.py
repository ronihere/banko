from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
    email = models.EmailField(default='none',unique=True)
    name = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return self.name
class TransactionDetails(models.Model):
    sender_data = models.CharField(default='none',max_length=50)
    receiver_data = models.CharField(default='none',max_length=50)
    amount_data = models.IntegerField(default='none')
    date=models.TextField(default='none',max_length=30)

    def __str__(self):
        return f"{self.sender_data}---->{self.receiver_data}----->{self.amount_data}"