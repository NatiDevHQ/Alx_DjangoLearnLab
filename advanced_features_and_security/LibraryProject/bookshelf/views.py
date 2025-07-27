
# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book  # make sure you have a Book model
from .forms import ExampleForm
from django.shortcuts import render, redirect

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def form_example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # safe processing
            form.save()  # or do something with validated data
            return redirect('book_list')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
