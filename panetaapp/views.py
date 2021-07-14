from django.shortcuts import render
from destinations.models import Destination
from blog.models import Post
# Create your views here.
def home(request):
    popular_destination = Destination.objects.filter(popular=True)[0:6]
    recent_post = Post.objects.filter(status="Published")[0:3]
    context = {

        'popular_dest': popular_destination,
        'recent_posts': recent_post
    }
    return render(request, 'index.html', context)

def handler404(request, exception):
    return render(request, '404.html', status=404)



def handler500(request):
    return render(request, '500.html', status=500)