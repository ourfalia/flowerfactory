from django.shortcuts import render

# Create your views here.


def news_letter(request):
    return render(request, 'newsletter/newsletter.html')
