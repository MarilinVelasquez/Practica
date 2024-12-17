from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Page

class PageListView(ListView):
    model = Page
    template_name = 'sample/home.html'  # Ruta de la plantilla que muestra la lista
    context_object_name = 'page_list'  # Nombre del contexto que usaremos en la plantilla

class PageDetailView(DetailView):
    model = Page
    template_name = 'sample/detail_view.html'  # Ruta de la plantilla que muestra el detalle de la página
    context_object_name = 'page'  # Nombre del contexto de la página
