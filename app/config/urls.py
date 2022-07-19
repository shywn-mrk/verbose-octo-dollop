from django.contrib import admin
from django.urls import path, include

from api.views import URLCreateView
from api.views import URLRetrieveView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('urls/', URLCreateView.as_view()),
    path('urls/<code>/', URLRetrieveView.as_view()),
]
