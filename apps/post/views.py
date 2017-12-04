from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from post.models import Article, Comment
from users.models import UserPro


def home(request):
    '''
    主页
    '''
    articles=Article.objects.all()
    return render(request, 'post/home.html', {'articles': articles})


def show(request):
    '''
    文章展示
    '''
    aid = int(request.GET.get('aid', 0))
    article = Article.objects.get(id=aid)

    comments = article.get_comments()
    return render(request, 'post/detail.html', {'article': article, 'comments': comments})


@login_required
def edit(request):
    '''
    编辑文章
    '''
    if request.method=='POST':
        aid = int(request.POST.get('aid', 0))
        article = Article.objects.get(id=aid)

        title = request.POST.get('title', '')
        content = request.POST.get('content', '')

        article.title = title
        article.content = content
        article.save()
        return redirect('/post/show/?aid=%d' % aid)
    else:
        aid = int(request.GET.get('aid', 0))
        article = Article.objects.get(id=aid)
        return render(request, 'post/edit.html', {'article': article})


def search(request):
    '''
    文章查询
    '''
    keyword = request.POST.get('keyword', '')
    result = Article.objects.filter(title__contains=keyword)
    return render(request, 'post/home.html', {'articles': result})


def comment(request):
    '''
    文章评论功能
    '''
    aid = int(request.POST.get('aid', 0))
    name = request.POST.get('name', '')
    content = request.POST.get('comment', '')
    Comment.objects.create(aid=aid, name=name, content=content)
    return redirect('/post/show/?aid=%d' % aid)

@login_required
def new_post(request):
    '''
    新建文章
    '''
    if request.method == 'POST':
        uid = int(request.POST.get('uid', 0))

        article =Article()
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        article.uid = uid
        article.title = title
        article.content = content
        article.save()
        return redirect(reverse('home'))
    else:

        return render(request, 'post/new_post.html')
