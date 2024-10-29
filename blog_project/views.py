from django.shortcuts import render
from posts.models import Post
from django.db.models import Q

def home(request):
    query = request.GET.get('q') 

    data = Post.objects.all()
    if query:
       
        data = data.filter(Q(title__icontains=query) | Q(category__name__icontains=query))  # Adjust according to your model

    return render(request, 'home.html', {'data': data, 'query': query})