from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import AddProductForm

from allauth.account.signals import user_signed_up
from django.dispatch import receiver


def product_in_category(request, category_slug=None ):   #함수형 카테고리
    current_category = None     #카테고리가 있을경우 없을경우 다 된다 .
    categories = Category.objects.all()         #모든 카테고리 가져온다 .
    product_types = ProductType.objects.all()       #타입 추가 park
    products = Product.objects.filter(available_display=True)       #제품을 보여줄수 있는것만 보여준다 . 관리자 모드에서 어빌리블 디스플레이 펄스인 애들은 안보여준다 .

    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)  #카테고리가 있는애들만 가져온다 .

        products = products.filter(category=current_category)       #불러온다 .

    return render(request, 'shop/list.html', {'current_category': current_category,     #변수 템플릿에 넘겨준다
                                              'product_types': product_types,
                                              'categories': categories,     #넘겨준 변수를 디스플레이해준다 .
                                              'products': products,
                                              })


def product_detail(request, id, product_slug=None): #뒤에 product_slug 는 urls에 있는 이름하고 같아야 된다 .
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity': 1})
    return render(request, 'shop/detail.html', {'product': product, 'add_to_cart': add_to_cart})


@receiver(user_signed_up)
def user_signed_up_(**kwargs):
    user = kwargs['user']
    extra_data = user.socialaccount_set.filter(provider='naver')[0].extra_data
    user.last_name = extra_data['name'][0:4]
    user.first_name = extra_data['name'][4:]
    user.save()
