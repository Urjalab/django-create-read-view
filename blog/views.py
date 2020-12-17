from django.shortcuts import render, redirect

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

            return redirect('/')
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

    if request.method == 'GET':

        post_obj = Post.objects.get(id=post_id) # exception generate
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

            post_model_obj = form_data.cleaned_data # dictionary

            post_model_obj = form_data.save(commit=False)
            old_post_model_obj = Post.objects.get(id=post_id)
            old_post_model_obj.title = post_model_obj.title            
            old_post_model_obj.content = post_model_obj.content  
            if post_model_obj.image is not None:
                old_post_model_obj.image =   post_model_obj.image         
            old_post_model_obj.save()

            return redirect('/')
        else:
            print(form_data.errors)
