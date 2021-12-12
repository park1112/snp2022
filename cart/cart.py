from decimal import Decimal
from django.conf import settings
from shop.models import Product
from coupon.models import Coupon


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_ID)
        if not cart:
            cart = self.session[settings.CART_ID] = {}
        self.cart = cart
        self.coupon_id = self.session.get('coupon_id')

    def __len__(self):  #카트에 몇개의 제품이 있는지 합하여 알려준다 . (quantity:수량)
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()  #제품들의 번호를 가져온다 .

        products = Product.objects.filter(id__in=product_ids)   #아이디가 위에 들어간 정보들 주세요 . 모든정보빼옴

        for product in products:    #하나씩 빼온다 . !
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():     #장바구니에 들어있는 제품을 업데이트 한다 .
            item['price'] = Decimal(item['price'])      #제품가격
            item['total_price'] = item['price'] * item['quantity']      #토탈 금액!

            yield item      #폴문을 돌릴때 아이템을 하나씩 던져준다 .

    def add(self, product, quantity=1, is_update=False):    #무조건 수량 1 넣어준다 . 장바구니에 담을때는 업데이트가 아니다.
        product_id = str(product.id)
        if product_id not in self.cart:     #프로젝트 아이디 넣어야됨.
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        if is_update:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:     #위에 제품을 찾아서 있으면 지운다 .
            del(self.cart[product_id])
            self.save()

    def clear(self):        #장바구니 비우기
        self.session[settings.CART_ID] = {}
        self.session['coupon_id'] = None
        self.session.modified = True

    def get_product_total(self):        #장바구니 들어있는 가격의 총합
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    @property
    def coupon(self):
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id)
        return None

    def get_discount_total(self):
        if self.coupon:
            if self.get_product_total() >= self.coupon.amount:
                return self.coupon.amount
        return Decimal(0)

    def get_total_price(self):
        return self.get_product_total() - self.get_discount_total()
