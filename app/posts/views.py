from django.core.cache import cache
from django.http import JsonResponse

from .models import Post


def post_view(request):
    posts = cache.get('posts')
    if not posts:
        posts = list(Post.objects.all().values('pk', 'text'))
        cache.set('posts', posts)
    return JsonResponse(posts, safe=False)
