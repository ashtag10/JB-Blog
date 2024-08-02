from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from .models import Comment


def home_view(request):
    #The method all() make the list of all the object's model
    if request.method =="GET":
        pl= Post.objects.all()
        return render(request, 'posts/post_list.html', {"post_list":pl})
 
def post_detail_view(request, pk):
    #The method get(id) permise to fetch element with his that we want to show detail 
    if request.method == "GET":
        pd= Post.objects.get(id=pk)
        cl= pd.comment_set.all()
        context={
            "post":pd,
            "comment_list":cl
        }
        return render(request, 'posts/post_detail.html', context)


def create_post_view(request):
    if request.method == "GET":
        pf= PostForm()
        return render(request, 'posts/post_create.html', {"form":pf})
    
    if request.method == "POST":
        pf= PostForm(data=request.POST)
        if pf.is_valid():
            post= pf.save(commit=False)
            post.author=request.user
            post.save()
            return redirect ('home')
        

    
def update_post_view(request,pk):
    if request.method == "GET":
        post= Post.objects.get(id=pk)
        form= PostForm(instance=post)
        return render(request, 'posts/post_update.html',{"form": form})
    
    if request.method == "POST":
        post= Post.objects.get(id=pk)
        form= PostForm(data=request.POST, instance=post)
        if form.is_valid():
            post=form.save()
            return redirect('post-detail', post.id)
        

def delete_post_view(request, pk):
    if request.method == "POST":
        post= Post.objects.get(id=pk)
        post.delete()
        return redirect('home')
    
def comment_create_view(request):
    if request.method =="POST":
        post_id=request.POST["post-id"]
        post=Post.objects.get(id=post_id)
        comment_text= request.POST["comment"]
        comment= Comment.objects.create(
            comment=comment_text,
            author=request.user,
            post=post
        )
        comment.save()
        return redirect('post-detail', post_id)

    