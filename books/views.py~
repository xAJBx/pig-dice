from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Books
from .filters import BookFilter
import requests


app_name = 'books'

def index(request):

    books = Books.objects.all()
    bookFilter = BookFilter(request.GET, queryset=books)
    books = bookFilter.qs
    context = {'books': books, 'bookFilter': bookFilter}
    return render(request, 'books/index.html', context)

def detail(request, books_id):
    book = get_object_or_404(Books, pk=books_id)
    # google books api request
    url = f'https://www.googleapis.com/books/v1/volumes/{book.google_books_id}'
    req = requests.get(url=url)
    google_response = req.json()
    try:
        google_res_desc = google_response['volumeInfo']['description']
    except KeyError:
        google_res_desc = ''
        
    book_main_title = book.title.partition(':')[0]
    book_sub_title = book.title.partition(':')[::-1][0]
    context = {'book': book, 'book_main_title': book_main_title,
               'book_sub_title': book_sub_title, 'google_response': google_response,
               'google_res_desc': google_res_desc}
    return render(request, 'books/detail.html', context)
