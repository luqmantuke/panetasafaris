from .models import Post
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.generic.list import ListView


def post_list(request):
    posts = Post.objects.filter(status="Published")
    popular_posts = Post.objects.filter(popular="Popular")[0:3]
    recent_post = Post.objects.filter(status="Published")[0:3]
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 15)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'popular_posts': popular_posts,
        'recent_posts': recent_post
    }

    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    query = Post.objects.filter(slug__iexact=slug)
    popular_posts = Post.objects.filter(popular="Popular")[0:3]
    recent_post = Post.objects.filter(status="Published")[0:3]

    if query.exists():
        query = query.first()

    context = {
        'post': query,
        'popular_posts': popular_posts,
        'recent_posts': recent_post
    }

    return render(request, 'blog/post_detail.html', context)


class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/blog_search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(name__icontains=query) | Q(body__icontains=query)
        )
        return object_list