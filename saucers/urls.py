from django.urls import path

from saucers.views import ListSaucers

urlpatterns = [
    path('get', ListSaucers.as_view(), name='saucers_list')
]
