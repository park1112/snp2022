import self as self
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accounts.decorators import account_ownership_required
from accounts.forms import AccountUpdateForm
from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]


def main(request):
    return render(request, 'base.html')


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm       ## html에 폼을 불러오면 이것이 불러와진다.
    success_url = reverse_lazy('accounts:main')
    template_name = 'accounts/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'     ##나만의 프로필로 들어갈 수 있다 .
    template_name = 'accounts/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object()).order_by('-pk')
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/delete.html'