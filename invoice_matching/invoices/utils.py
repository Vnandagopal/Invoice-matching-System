import PyPDF2
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        return text




def preprocess_text(text):
    if text is None:
        return ""
    text = re.sub(r'\W+', ' ', text) #converts every non word character to space
    text = text.lower()

    return text

def vectorize_text(texts):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)

    return  vectors, vectorizer

def find_most_similar_invoice(input_vectors, database_vectors):
    similarities = cosine_similarity(input_vectors, database_vectors)
    most_similar_index = similarities.argmax()
    return most_similar_index, similarities[0, most_similar_index]







