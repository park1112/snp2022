from django.urls import path
from django.views.generic import TemplateView

from client.views import client_in_expertise

app_name = 'client'

urlpatterns = [
    # path('list/', ArticleListView.as_view(), name='list'),
    #
    path('create/', client_in_expertise, name='create'),
    # path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    # path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]
