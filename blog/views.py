from django.shortcuts import render

posts = [
    {
        "author" : "Yash Varshney",
        "title" : "Blog Post 1",
        "content" : "First post content",
        "date_posted" : "May 03, 2024",
        "date_updated" : "May 03, 2024"
    },
    {
        "author" : "Shubh Varshney",
        "title" : "Blog Post 2",
        "content" : "Second post content",
        "date_posted" : "May 01, 2024",
        "date_updated" : "May 02, 2024"
    }

]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})