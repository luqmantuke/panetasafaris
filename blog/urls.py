from django.urls import path
from .views import post_list, post_detail, SearchResultsView

urlpatterns = [
    path('blog/', post_list, name="post_list"),
    path('blog/<slug:slug>/', post_detail, name="post_detail"),
    path('blog/search/', SearchResultsView.as_view(), name="blogsearch")
]
