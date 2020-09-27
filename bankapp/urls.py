from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ImageUploadView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = {
    url(r'', csrf_exempt(ImageUploadView.as_view())),
    
}
urlpatterns = format_suffix_patterns(urlpatterns)