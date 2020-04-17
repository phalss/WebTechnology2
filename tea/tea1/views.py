from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView, TemplateView
import os
import fnmatch

class HomeView(TemplateView):
    template_name = "base.html"

class PredictionView(TemplateView):
    template_name = "visualizing_trading_strategy.html"

def display_video(request,vid=None):
    if vid is None:
        return HttpResponse("No Video")

    #Finding the name of video file with extension, use this if you have different extension of the videos    
    video_name = "yo.mp4"
    for fname in os.listdir(settings.MEDIA_ROOT):
        if fnmatch.fnmatch(fname, vid+".*"): #using pattern to find the video file with given id and any extension
            video_name = fname
            break


    '''
        If you have all the videos of same extension e.g. mp4, then instead of above code, you can just use -

        video_name = vid+".mp4"

    '''

    #getting full url - 
    video_url = settings.MEDIA_URL+video_name

    return render(request, "base.html", {"url":video_url})

    def predictions(request):
        return render(request, 'templates/predictions.html')