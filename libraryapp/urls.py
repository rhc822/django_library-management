from django.urls import include, path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('librarians/', librarian_list, name='librarians'),
    path('logout/', logout_user, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('books/form', book_form, name='books_form'),
]