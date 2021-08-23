from django.shortcuts import render, redirect
from lists.models import Item


def home_page(request):
    """home page"""
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/one-and-only-list-in-the-world/')
    return render(request, 'home.html')


def view_list(request):
    """new list"""
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
