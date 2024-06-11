from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import LoginForm
from .models import User
from .models import adUser
from .forms import SignupForm
from .forms import adSignupForm
from .forms import adLoginForm
from .models import User
from .models import Feedback
from .forms import FeedbackForm
from .models import CartItem
from .models import Product,Order
from .forms import ProductForm,Adstore

def home(request):
    feedback_entries = Feedback.objects.all()
    products = Product.objects.all()
    return render(request, "index.html", {'feedback_entries': feedback_entries , 'products': products})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def shop(request):
    products = Product.objects.all()
    return render(request, 'watchs.html', {'products': products})

def review(request):    
    feedback_entries = Feedback.objects.all()
    return render(request, "testimonial.html", {'feedback_entries': feedback_entries})

def login(request):
    return render(request, "login.html")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            new_password = form.cleaned_data['new_password']
            if User.objects.filter(username=username).exists():
                error_message = "Username is already taken."

                return render(request, 'signup.html', {'form': form, 'error_message': error_message})
            if password!=new_password:
                error_message1 = "Passwords Do not match."
                return render(request, 'signup.html', {'form': form, 'error_message': error_message1})
            else:
                user = User.objects.create(username=username, password=password)
                return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username, password=password)
                request.session['username'] = username
                return render(request, 'indexlog.html')
            except User.DoesNotExist:
                error_message = "Invalid username or password."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def adsignup(request):
    if request.method == 'POST':
        form = adSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            new_password = form.cleaned_data['new_password']
            if adUser.objects.filter(username=username).exists():
                error_message = "Username is already taken."

                return render(request, 'admin_signup.html', {'form': form, 'error_message': error_message})
            if password!=new_password:
                error_message1 = "Passwords Do not match."
                return render(request, 'admin_signup.html', {'form': form, 'error_message': error_message1})
            else:
                aduser = adUser.objects.create(username=username, password=password)
                return redirect('adlogin')
    else:
        form = SignupForm()
    return render(request, 'admin_signup.html', {'form': form})

def adlogin(request):
    if request.method == 'POST':
        form = adLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                aduser = adUser.objects.get(username=username, password=password)
                return render(request, 'product_list.html')
            except adUser.DoesNotExist:
                error_message = "Invalid username or password."
                return render(request, 'admin_log.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'admin_log.html', {'form': form})

def homelog(request):
    feedback_entries = Feedback.objects.all()
    products = Product.objects.all()
    return render(request, "indexlog.html", {'feedback_entries': feedback_entries , 'products': products})

def aboutlog(request):
    return render(request, "aboutlog.html")

def contactlog(request):
    return render(request, "contactlog.html")

def testimoniallog(request):
    feedback_entries = Feedback.objects.all()
    return render(request, "testimoniallog.html", {'feedback_entries': feedback_entries})

def testimoniallog(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            feedback_entries = Feedback.objects.all()
            return render(request, 'testimoniallog.html', {'feedback_entries': feedback_entries})
    else:
        form = FeedbackForm()
    feedback_entries = Feedback.objects.all()
    return render(request, "testimoniallog.html", {'form': form,'feedback_entries': feedback_entries})

def shoplog(request):
    products = Product.objects.all()
    return render(request, 'watchslog.html', {'products': products})

def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        image = request.POST.get('image')
        name = request.POST.get('name')
        price = request.POST.get('price')
        existing_item = CartItem.objects.filter(name=name).first()
        if existing_item:
            existing_item.quantity += 1
            existing_item.save()
        else:
            CartItem.objects.create(name=name, image=image, price=price)
        return redirect('cart')
    return render(request, "watchlog.html")

def cart(request):
    cart_items = CartItem.objects.all()
    username = request.session.get('username')
    for item in cart_items:
        item.total_price = item.price * item.quantity
    total_price = sum(item.total_price for item in cart_items)
    if request.method == 'POST':
        form = Adstore(request.POST)
        if form.is_valid():
            form.save()
            CartItem.objects.all().delete()
            message = "Your order has been placed successfully!"
            return render(request, 'cart.html', { 'message': message})
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price ,'username': username})

def update_quantity(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'increase':
            item.quantity += 1
        elif action == 'decrease':
            if item.quantity > 1:
                item.quantity -= 1
        item.save()
    return redirect('cart')

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id)
    item.delete()
    return redirect('cart')

def product_list(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'product_list.html', {'products': products, 'form': form})
    else:
        form = ProductForm()
    return render(request, 'product_list.html', {'products': products, 'form': form})

def adfeedback(request):
    feedback_entries = Feedback.objects.all()
    return render(request, "adfeedback.html", {'feedback_entries': feedback_entries})

def delete_feedback(request, feedback_id):
    if request.method == 'POST':
        feedback = Feedback.objects.get(pk=feedback_id)
        feedback.delete()
    return redirect('adfeedback')

def remove_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.delete()
    return redirect('product_list')

def order(request):
    orders = Order.objects.all()
    return render(request, "adorders.html", {'orders': orders})

def complete_order(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        if order_id:
            order_to_delete = Order.objects.get(pk=order_id)
            order_to_delete.delete()
    return redirect('order')