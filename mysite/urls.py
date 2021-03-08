from django.contrib import admin
from django.urls import path, include
from core.views import *


urlpatterns = [
    path('', home, name="home"),
    path('signup/', signup, name="signup"),
    path('secret/', secret_page, name="secret"),
    path('secret2', SecretPage.as_view(), name="secret2"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
