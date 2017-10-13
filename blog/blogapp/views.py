from django.shortcuts import render,HttpResponse,redirect
from blogapp.models import Aritcle,Comment

from django.template import Context,Template
from blogapp.form import CommentForm
from django.core.paginator import Paginator


def first(request):
    context = {}
    article_list = Aritcle.objects.all()
    context['article_list'] = article_list
    first_page = render(request,'first_page.html',context)
    return first_page



def index(request):
    #第一个GET是字典；第二个get是方法；判断传递参数
    queryset = request.GET.get('tag')
    if queryset:
        article_list = Aritcle.objects.filter(tag=queryset)
    else:
        article_list = Aritcle.objects.all()
    context = {}
    context['article_list'] = article_list
    index_page = render(request,'index.html',context)
    return index_page


def detail(request,page_num):

    if request.method == "GET":
        form = CommentForm

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            a = Aritcle.objects.get(id=page_num)
            c = Comment(name = name,comment = comment,belong_to=a)
            c.save()
            return redirect(to=detail,page_num=page_num)
    context = {}
    #comment_list = Comment.objects.all()
    article = Aritcle.objects.get(id=page_num)
    context['article'] = article
    #context['comment_list'] = comment_list
    context['form'] = form
    return render(request, 'detail.html', context)
