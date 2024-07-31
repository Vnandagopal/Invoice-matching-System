import logging
from django.core.management.base import BaseCommand
from invoices.models import Invoice

class Command(BaseCommand):
    help = 'Prints all invoices in the database'

    def handle(self, *args, **kwargs):
        invoices = Invoice.objects.all()
        if not invoices:
            self.stdout.write("No invoices found.")
        for invoice in invoices:
            self.stdout.write(f"ID: {invoice.id}")
            self.stdout.write(f"PDF: {invoice.pdf}")
            self.stdout.write(f"Text: {invoice.text}")
            self.stdout.write(f"Created At: {invoice.created_at}")
            self.stdout.write("-" * 20)
