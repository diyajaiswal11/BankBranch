from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import IFSCView, CityBankView

urlpatterns = {
    url(r'^ifsc/(?P<ifsc>[A-Za-z]{4}\w{7})$', IFSCView.as_view()),
    url(r'^branches/(?P<city>.*)/(?P<bankname>.*)$', CityBankView.as_view())
}

urlpatterns = format_suffix_patterns(urlpatterns)