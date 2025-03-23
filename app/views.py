from django.shortcuts import render
from django.views import View
from .forms import RegistrationForm
from django.contrib import messages


from app.models import (
    Customer,
    Product,
    Cart,
    OrderPlaced
)

class ProductView(View):
    def get(self, request):
        men = Product.objects.filter(category='MF')
        women = Product.objects.filter(category='WF')
        shoes = Product.objects.filter(category='Sh')
        context = {
            'men': men,
            'women': women,
            'shoes': shoes
        }
        return render(request, 'index.html', context)


class ProductDetailView(View):
    def get(self, request, id):
        product = Product.objects.get(pk=id)
        return render(request, 'productDetails.html', {'product': product})


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'registration.html', {'form': form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'registration.html', {'form': form})



def shoes(request, data=None):
    if data == None:
        shoes = Product.objects.filter(category='Sh')
    elif data == 'Campus' or data == "Samsung":
        shoes = Product.objects.filter(category='Sh').filter(brand=data)
    elif data == 'below':
        shoes = Product.objects.filter(category='Sh').filter(discounted_price__lt=100)
    return render(request, 'shoes.html', {'shoes': shoes}) 


def profile(request):
    return render(request, 'profile.html')


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('pro_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return render(request, 'addToCart.html')

def cart(request):
    if request.user.is_authenticated:
        user = request.user
        carts = Cart.objects.filter(user=user)
        total = 0
        for cart in carts:
            total += cart.product.discounted_price * cart.quantity

        return render(request, 'addToCart.html', {'carts': carts, 'total': total})
