from multiprocessing import context
from django.views.generic import TemplateView
#from .models import Certificado, Projeto, Tecnologia, Habilidade, Livro

class CurriculoView(TemplateView):
    template_name = 'curriculo.html'

    #def get_context_data(self, **kwargs):
        #context = super(IndexView, self).get_context_data(**kwargs)
        #context['certificado'] = Certificado.objects.order_by('?').all()
        #return context