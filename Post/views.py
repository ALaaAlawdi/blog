from django.shortcuts import render , redirect 
from django.shortcuts import get_object_or_404 
  


from .models  import Post
from .forms import PostForm

# Create your views here.
def all_post(request):
    all_posts = Post.objects.all()
    context = {'all_posts' : all_posts , }
    return render( request , "all_posts.html" , context)

def post(request , id ):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post , id=id )
    context ={"post" : post , }
    return render(request , "detail.html" , context )
    

def create_post(request):
    if request.method== 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/')

    else:
        form  = PostForm()

    context ={
        'form': form ,'post':post ,
    }
    return render(request , "create.html" , context )


def edit_post(request , id ):
        post = get_object_or_404(Post , id = id )
        if request.method == 'POST':
             form = PostForm(request.POST , instance=post)
             if form.is_valid():
                  new_form = form.save(commit=False)
                  new_form.user = request.user  
                  new_form.save()
                  return redirect('/')
        
        else:
             form = PostForm(instance=post)
        
        context = {
             'form':form , 'post':post ,
        }

        return render(request ,  'edit.html' , context) 