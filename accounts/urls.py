from django.urls import reverse, path, include
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup")
]
