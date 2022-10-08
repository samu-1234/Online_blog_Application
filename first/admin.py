from django.contrib import admin
from first.models import Reg,Login
# Register your models here.
from .models import BlogInfo, Login, Reg,Comment
admin.site.register(Reg)
admin.site.register(Login)
admin.site.register(BlogInfo)
admin.site.register(Comment)