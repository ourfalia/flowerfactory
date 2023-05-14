from django.shortcuts import render
from .models import Aboutus, Why_Chose_Us




def aboutus_list(request):
    aboutus = Aboutus.objects.all()
    why_chose_us = Why_Chose_Us.objects.all()


    context = {
        'aboutus': aboutus,
        'why_chose_us': why_chose_us,
    }

    return render(request, 'aboutus/aboutus.html', context)
