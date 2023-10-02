from django.db import models

# Create your models here.
class Invoice(models.Model):
    date = models.DateField()
    customer_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Invoice {self.id}"

class InvoiceDetail(model.Models):
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE,related_names="details")
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.id
    
