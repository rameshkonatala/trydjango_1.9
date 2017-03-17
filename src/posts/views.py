from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
# Create your views here.


def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Successfully created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request,"Not Successfully created")
	context = {
		"form":form,
	}
	return render(request,"post_form.html",context)

def post_detail(request,id):
	instance  = get_object_or_404(Post,id=id)
	context={
		"title":instance.title,
		"instance":instance,
	}
	return render(request,"post_detail.html",context)

def post_list(request):
	queryset = Post.objects.all()
	context={
		"object_list":queryset,
		"title":"List"
	}
	return render(request,"post_list.html",context)
	#return HttpResponse("<h1>List</h1>")

def post_update(request,id=None):
	instance = get_object_or_404(Post,id=id)
	form = PostForm(request.POST or None,instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Item updated")
		return HttpResponseRedirect(instance.get_absolute_url())		
	context={
		"title":instance.title,
		"instance":instance,
		"form":form,
	}
	return render(request,"post_form.html",context)

def post_delete(request,id=None):
	instance = get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request,"Item deleted")
	return redirect("posts:lists")