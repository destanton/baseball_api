"""baseball_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from baseball_data.views import MasterListCreateAPIView, BattingListCreateAPIView, FieldingListCreateAPIView,\
                                PitchingListCreateAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/masters/$', MasterListCreateAPIView.as_view(), name="master_list_create_api_view"),
    url(r'^api/battings/$', BattingListCreateAPIView.as_view(), name="batting_list_create_api_view"),
    url(r'^api/fieldings/$', FieldingListCreateAPIView.as_view(), name="fielding_list_create_api_view"),
    url(r'^api/pitchings/$', PitchingListCreateAPIView.as_view(), name="pitching_list_create_api_view")
]
