from django.shortcuts import render
from django.http import HttpResponse

# Головна сторінка
def home(request):
    return render(request, 'home.html', {'title': 'Магазин іграшок mememm'})

# Про нас
def about(request):
    return render(request, 'about.html', {'title': 'Про нас'})

# Сторінка з товарами
def toys(request):
    return render(request, 'toys.html', {'title': 'Наші іграшки'})

# Контакти
def contacts(request):
    return render(request, 'contacts.html', {'title': 'Контакти'})
