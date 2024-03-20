from django.db import models
# coder :- sudarshan date


class Expense(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField()
    category = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
