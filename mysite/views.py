from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.conf import settings
import os
# Create your views here.
def index(request):
	context = {'MEDIA_URL': settings.MEDIA_URL,
				'STATIC_URL': settings.STATIC_URL}
	return(render_to_response('templates/index.html', context))



def pdf_view(request):
	with open(os.path.join(settings.MEDIA_ROOT,'resume.pdf'), 'rb') as pdf:
		response = HttpResponse(pdf.read(),content_type='application/pdf')
		return response


def cv_view(request):
	with open(os.path.join(settings.MEDIA_ROOT,'CV.pdf'), 'rb') as pdf:
		response = HttpResponse(pdf.read(),content_type='application/pdf')
		return response

def slides_selection(request, slides_name):
	slide_path = slides_name + ".pdf"
	with open(os.path.join(settings.MEDIA_ROOT, slide_path), 'rb') as pdf:
		response = HttpResponse(pdf.read(),content_type='application/pdf')
		return response

def slides(request):
	context = {'MEDIA_URL': settings.MEDIA_URL,
				'STATIC_URL': settings.STATIC_URL}
	return(render_to_response('templates/slides.html', context))



