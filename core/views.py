from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, Order
from .forms import OrderForm
from .cart import Cart

def home(request):
    products = Product.objects.all()
    form = OrderForm()
    context = {
        'products': products,
        'form': form,
    }
    return render(request, 'core/home.html', context)

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            messages.success(request, f'Заказ #{order.id} успешно оформлен! Мы свяжемся с вами в ближайшее время.')
            return redirect('home')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = OrderForm()
    
    products = Product.objects.all()
    context = {
        'products': products,
        'form': form,
    }
    return render(request, 'core/home.html', context)