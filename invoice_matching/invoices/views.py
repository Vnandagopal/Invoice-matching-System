from django.shortcuts import render,redirect
from .forms import InvoiceForm
from .models import Invoice
from .utils import extract_text_from_pdf, preprocess_text, vectorize_text, find_most_similar_invoice

# Create your views here.
def home(request):
    return render(request, 'home.html')
def upload_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            invoice = form.save()
            text = extract_text_from_pdf(invoice.pdf.path)
            invoice.text = preprocess_text(text)
            invoice.save()

            return redirect('match_invoice',invoice_id =invoice.id)

    else:
        form = InvoiceForm()
    return render(request, 'upload_file.html', {'form':form})


def match_invoice(request, invoice_id):
    invoice = Invoice.objects.get(id = invoice_id)
    invoices = Invoice.objects.exclude(id = invoice_id)

    database_texts =  [inv.text or '' for inv in invoices if inv.text]
    input_text = invoice.text or ""

    if not database_texts:
        # If there are no other invoices to compare against
        return render(request, 'match_invoice.html', {
            'input_invoice': invoice,
            'most_similar_invoice': None,
            'similarity_score': None,
            'message': 'No other invoices available for comparison.'
        })


    texts = [input_text] + database_texts
    vectors, vectorizer = vectorize_text(texts)

    input_vector = vectors[0]
    database_vectors = vectors[1:]
    most_similar_index, similarity_score = find_most_similar_invoice(input_vector, database_vectors)
    most_similar_index = int(most_similar_index)
    most_similar_invoice= invoices[most_similar_index]

    return render(request, 'match_invoice.html',{
       'input_invoice':invoice,
        'most_similar_invoice': most_similar_invoice,
        'similarity_score': similarity_score,
        'most_similar_invoice_pdf_url': most_similar_invoice.pdf.url,
        'input_invoice_pdf_url':invoice.pdf.url
})







