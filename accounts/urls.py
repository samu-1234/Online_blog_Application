from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("accounts.urls")),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',views.index,name="home"),
    path('accounts/sign_up/',views.sign_up,name="sign-up")
]



# from django.contrib import admin
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('',views.index,name="home"),
#     path('accounts/sign_up/',views.sign_up,name="sign-up")
# ]