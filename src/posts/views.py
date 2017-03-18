from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
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
	queryset_list = Post.objects.all()#.order_by("-timestamp")
	paginator = Paginator(queryset_list, 2) # Show 25 contacts per page
	page_request_var = 'set'
	page = request.GET.get(page_request_var)
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)

	context={
		"object_list":queryset,
		"title":"List",
		"page_request_var":page_request_var
	}
	return render(request,"post_list.html",context)
	#return HttpResponse("<h1>List</h1>")



def listing(request):
    contact_list = Contacts.objects.all()


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