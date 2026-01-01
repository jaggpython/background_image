from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import SignupForm, ProductForm
from .models import Product


# ---------------- AUTH ---------------- #

def signup_view(request):
    form = SignupForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, "home.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )

        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    products = Product.objects.all()

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.is_active = request.POST.get("is_active") == "on"
            product.save()
            messages.success(request, "Product saved successfully")
            return redirect("dashboard")
    else:
        form = ProductForm()

    return render(request, "dashboard.html", {
        "products": products,
        "form": form
    })





# ---------------- PRODUCTS (CRUD) ---------------- #

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


@login_required
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Product added successfully")
        return redirect('product_list')

    return render(request, 'product_form.html', {
        'form': form,
        'title': 'Add Product'
    })


@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Product updated successfully")
        return redirect('dashboard')

    return render(request, 'product_form.html', {
        'form': form,
        'title': 'Edit Product'
    })


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully")
        return redirect('dashboard')

    return render(request, 'product_confirm_delete.html', {
        'product': product
    })

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})
