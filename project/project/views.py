
from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse, Http404


def favicon(request):
    file_path = os.path.join(settings.STATIC_ROOT, 'favicon.ico')
    try:
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="image/webp,image/apng,image/*,*/*;q=0.8")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
    except:
        raise Http404


def index(request):
    return render(request, template_name='index.html')

