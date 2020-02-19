from django.conf.urls import url
from .views import UserRegistrationView

import pdb; pdb.set_trace()
urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view()),
    ]