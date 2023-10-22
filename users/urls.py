from django.urls import path, include

from .views import UserCreateView

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('register/', UserCreateView.as_view(), name='user-create'),
]
