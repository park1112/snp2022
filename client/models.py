from django.db import models
from django.urls import reverse




class Expertise(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)     #카테고리 설명

    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True, verbose_name="Slog(검색을위한)") #

    class Meata:        # 기본정렬값 , 이름 , 카테고리 , 순
        ordering = ['name']
        verbose_name = 'expertise'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name        #카테고리 나타낼 이름

    def get_absolute_url(self):     #상세페이지
        return reverse('client:client_in_expertise', args=[self.slug])

class CompanyName(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.TextField(blank=True)     #카테고리 설명

    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True, verbose_name="Slog(검색을위한)") #

    class Meata:        # 기본정렬값 , 이름 , 카테고리 , 순
        ordering = ['name']
        verbose_name = 'companyname'    #admin 카테고리 나타낼때 단수형
        verbose_name_plural = 'companynames'      #admin 카테고리 나타낼때 복수형

    def __str__(self):
        return self.name        #카테고리 나타낼 이름

    def get_absolute_url(self):     #상세페이지
        return reverse('shop:product_in_category', args=[self.slug])




class Client(models.Model):
    expertise = models.ForeignKey(Expertise, on_delete=models.SET_NULL, null=True, related_name='representatives', verbose_name="구분")   #카테고리가 삭제되어도 제품은 삭제되지 않는다 , 삭제가능, 카테고리 입장에서 어떻게 불러올거야? 별도의 이름 설정
    companyname = models.ForeignKey(CompanyName, on_delete=models.SET_NULL, null=True, related_name='companynames', verbose_name="소속회사")
    name = models.CharField(max_length=50, db_index=True, verbose_name="이름")
    slug = models.SlugField(max_length=50, db_index=True, unique=True, allow_unicode=True, verbose_name="Slog(검색을위한)")
    email = models.EmailField(blank=True, null=True)


    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True, db_index=True, verbose_name="휴대폰")  # Here
    fax_number = models.CharField(max_length=14, null=True, blank=True, verbose_name="팩스번호")  # Here
    image = models.ImageField(upload_to='client/%Y/%m/%d', blank=True)
    personal_number = models.CharField(max_length=14, unique=True, db_index=True, null=True, blank=True, verbose_name="주민등록번호")
    business_number = models.CharField(max_length=14, unique=True, db_index=True,null=True, blank=True, verbose_name="사업자번호")
    crprt_rgnmb = models.CharField(max_length=20, unique=True, db_index=True, null=True, blank=True, verbose_name="법인등록번호")
    bank = models.CharField(max_length=200, null=True, blank=True, verbose_name="결제은행")
    bank_number = models.CharField(max_length=200, null=True, blank=True, verbose_name="계좌번호")

    address = models.CharField(max_length=250, null=True, blank=True, verbose_name="주소")
    description = models.TextField(blank=True, verbose_name="설명")


    meta_description = models.TextField(blank=True)

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