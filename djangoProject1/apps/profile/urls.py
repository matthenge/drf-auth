from django.conf.urls import url
from djangoProject1.apps.profile.views import UserProfileView


urlpatterns = [
    url(r'^profile', UserProfileView.as_view()),
]