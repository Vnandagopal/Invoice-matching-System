from django.db import models

# Create your models here.

class Invoice(models.Model):
    pdf = models.FileField(upload_to='invoices/')
    text = models.TextField(null=True, blank=True, )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.id}"