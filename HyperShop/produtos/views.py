from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Produto, Cliente


class ProdutoListView(generic.ListView):
    model = Produto
    template_name = "index.html"

    # def get_absolute_url(self):
    #     return reverse('livro_detail', args=[(str(self.id))])

class EnderecoListView(generic.ListView):
    model = Cliente

class CadastroEnderecoView(generic.CreateView):
    model = Cliente
    fields = ['documento', 'endereco', 'cep', 'numero_residencia', 'uf', 'telefone']
    template_name = 'produtos/cadastro_endereco.html'
    success_url = reverse_lazy('endereco')

class EditEnderecoView(LoginRequiredMixin, generic.UpdateView):
    model = Cliente
    fields = ['documento', 'endereco', 'cep', 'numero_residencia', 'uf', 'telefone']
    template_name = 'produtos/cadastro_endereco.html'
    success_url = reverse_lazy('endereco')