from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)     #카테고리 설명

    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True, verbose_name="Slog(검색을위한)") #

    class Meata:        # 기본정렬값 , 이름 , 카테고리 , 순
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name        #카테고리 나타낼 이름

    def get_absolute_url(self):     #상세페이지
        return reverse('shop:product_in_category', args=[self.slug])

class ProductType(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)     #카테고리 설명

    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True, verbose_name="Slog(검색을위한)") #

    class Meata:        # 기본정렬값 , 이름 , 카테고리 , 순
        ordering = ['name']
        verbose_name = 'product_type'    #admin 카테고리 나타낼때 단수형
        verbose_name_plural = 'product_types'      #admin 카테고리 나타낼때 복수형

    def __str__(self):
        return self.name        #카테고리 나타낼 이름

    def get_absolute_url(self):     #상세페이지
        return reverse('shop:product_in_category', args=[self.slug])




class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products', verbose_name="품명")   #카테고리가 삭제되어도 제품은 삭제되지 않는다 , 삭제가능, 카테고리 입장에서 어떻게 불러올거야? 별도의 이름 설정
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, related_name='types', verbose_name="종류(KG)")
    name = models.CharField(max_length=200, db_index=True, verbose_name="이름")
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True, verbose_name="Slog(검색을위한)")

    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True, verbose_name="설명")
    meta_description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="금액")    #몇자리까지?, 소수점은 몇자리까지 ?
    stock = models.PositiveIntegerField(verbose_name="수량")

    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meata:
        ordering = ['-created']
        index_together = [['id','slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])