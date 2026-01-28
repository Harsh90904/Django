from django.http import HttpResponse
from django.template import loader
from .models import Member

def home(request):
  mydata = Member.objects.all().values()
  template = loader.get_template('myfirst.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

def culture(request):
  template = loader.get_template('culture.html')
  return HttpResponse(template.render({}, request))

def history(request):
  template = loader.get_template('history.html')
  return HttpResponse(template.render({}, request))
