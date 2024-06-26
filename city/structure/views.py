from django.http import HttpResponse
from django.template import loader

def main_page(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def news_page(request):
  template = loader.get_template('news.html')
  return HttpResponse(template.render())

def main_admin(request):
  template = loader.get_template('admin_site.html')
  return HttpResponse(template.render())

def main_facts(request):
  template = loader.get_template('facts.html')
  return HttpResponse(template.render())

def main_contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def history_page(request):
  template = loader.get_template('history.html')
  return HttpResponse(template.render())
def people_page(request):
  template = loader.get_template('people.html')
  return HttpResponse(template.render())
def photos_page(request):
  template = loader.get_template('photos.html')
  return HttpResponse(template.render())