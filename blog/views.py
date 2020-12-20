from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .models import Post
from .forms import PostForm

# Create View using Django Forms : https://tutorial.djangogirls.org/en/django_forms/

def read_view(request):

    blogs = Post.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(
        request,
        'blog/read.html',
        context
    )

def create_view(request):


    if request.method == 'POST':
        form_data = PostForm(request.POST, request.FILES)

        if form_data.is_valid():

            # https://stackoverflow.com/a/12848678/9755816
            post_model_obj = form_data.save(commit=False)

            user = request.user
            post_model_obj.posted_by = user
            
            post_model_obj.save()

            return redirect('home_page')
        else:
            print(form_data.errors)



    form = PostForm()
    context = {
        'form': form,
    }

    return render(
        request,
        'blog/create.html',
        context
    )

def update_view(request, post_id):

    post_obj = Post.objects.get(id=post_id) 

    if request.method == 'GET':

        # exception generate
        form = PostForm(instance=post_obj)

        context = {
            'form': form
        }

        return render(
            request,
            'blog/update.html',
            context
        )

    elif request.method == 'POST':

        form_data = PostForm(request.POST, request.FILES)

        if form_data.is_valid():

            # https://stackoverflow.com/a/12848678/9755816
            data = form_data.cleaned_data  # returns dictionary of valid form fields.

            post_obj.title = data.get('title')
            post_obj.content = data.get('content')

            if data.get('image') is None:
                pass
            else:
                post_obj.image = data.get('image')

            post_obj.save()
            return redirect('home_page')
        else:
            return HttpResponse(str(form_data.errors))

@require_POST # compels to accept only POST request.
def delete_view(request, post_id):

    post_obj = Post.objects.get(id=post_id) # generate exception

    post_obj.delete()

    return redirect('home_page')
