from django.contrib import admin
from apps.accounts.models import User, Post

admin.AdminSite.site_header = "Nadja"
admin.AdminSite.site_title = "Nadja"
admin.AdminSite.site_url = None


admin.site.register(User)
admin.site.register(Post)
