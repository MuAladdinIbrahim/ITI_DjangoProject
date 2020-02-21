from django.shortcuts import render
from django.http import HttpResponse
from .models import Post , Category ,Comments,Reply

def homePage(request):
	posts = Post.objects.all().order_by('date')
	cats = Category.objects.all()
	context={'posts':posts,'cats':cats}
	return render(request,'posts/index.html', context)

def about(request):
	return render(request,'posts/about.html')

def displayPost(request,postid):
	post = Post.objects.get(id=postid)
	comments = Comments.objects.filter(post_name_id=postid)
	data = []
	for comment in comments :
		reply = Reply.objects.get(comment_name_id=comment.id)
		dic = {'comm':comment , 'rep':reply}
		data.append(dic)

	context={'post':post,'data':data}
	return render(request, 'posts/single.html',context)

def listCat(request,catid):
	posts = Post.objects.filter(cat_name_id=catid)
	cats = Category.objects.all()
	context={'posts':posts,'cats':cats}
	return render(request,'posts/index.html', context)
