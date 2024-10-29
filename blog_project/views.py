from django.shortcuts import render
from posts.models import Post

def home(request):
    query = request.GET.get('q') 
    if query:
        data = Post.objects.filter(title__icontains=query)  
    else:
        data = Post.objects.all()  

    return render(request, 'home.html', {'data': data})