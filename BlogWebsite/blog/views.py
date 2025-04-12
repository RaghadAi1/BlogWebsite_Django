from django.http import HttpResponse
from django.template import loader
from .models import User, Post, Comment, Category
# Create your views here.



def blogs(request):
    blog = blogs.objects.all().values()
    template = loader.get_template('blogs.html')
    context = {
        'blog': blog,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def blog_details(request):
    # var from users
    Users = users.objects.get(id=id)
    template = loader.get_template('blog_details.html')
    context = {
    'Users': users,
}
    return HttpResponse(template.render(context, request))


def users(request):
    Users = users.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'users': Users,
    }
    return HttpResponse(template.render())


def comments(request):
    comments = comments.objects.all().values()
    template = loader.get_template('comments.html')
    context = {
        'comments': comments,
    }
    return HttpResponse(template.render(context, request))

def categories(request):
    cat = categories.objects.all().values()
    template = loader.get_template('categories.html')

    context = {
        'cat': categories,
    }
    return HttpResponse(template.render(context, request))     


# python3 manage.py migrate
# python3 manage.py runserver