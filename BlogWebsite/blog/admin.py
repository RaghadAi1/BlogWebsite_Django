from django.contrib import admin

# Register your models here.
from .models import User, Post, Comment, Category

class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "Username", "Email")
admin.site.register(User, UserAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "category", "Date_Published")
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("post_id", "user_id", "Content", "Date_Posted")
admin.site.register(Comment, CommentAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","id")
admin.site.register(Category, CategoryAdmin)
# if you want the admin page work correctly, you need to add the following lines in the settings.py file
# python -m venv .venv
# source .venv/bin/activate
# python3 --version
# python manage.py makemigrations
# python manage.py migrate
# python3 manage.py createsuperuser
# python3 manage.py runserver
# pip install django
# install django-admin
# http://127.0.0.1:8000/admin/login/?next=/admin/
