from django.urls import path
from .views import *

app_name = 'shop'   #이걸 지정해줘야지 모델에 reverse('shop:product_detail') 이렇게 사용할수 있다 .

urlpatterns = [
    path('', product_in_category, name='product_all'),
    path('<category_slug>/', product_in_category, name='product_in_category'),
    path('<int:id>/<product_slug>/', product_detail, name='product_detail'),
]