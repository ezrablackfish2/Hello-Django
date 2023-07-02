from django.urls import path
from .views import BlogListVeiw

urlpatterns = [
        path = ("", BlogListView.as_view(), name="home"),
]
