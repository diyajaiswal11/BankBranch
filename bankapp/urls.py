from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import IFSCView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = {
    url(r'', csrf_exempt(IFSCView.as_view())),
    
}
urlpatterns = format_suffix_patterns(urlpatterns)