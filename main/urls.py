
from django.urls import path
from . import views
# from .views import MainListView



urlpatterns = [
    # path('', views.mainView, name='main-view'),
    path('', views.MainListView.as_view(), name='main-view'),
]
