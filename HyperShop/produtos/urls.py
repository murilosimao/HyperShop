from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.ProdutoListView.as_view(), name='produtos'),
    path('endereco', views.EnderecoListView.as_view(), name='endereco'),
    path('endereco/cadastro', views.CadastroEnderecoView.as_view(), name='cadastro_endereco'),
    path('endereco/<int:pk>/editar', views.EditEnderecoView.as_view(), name='editar_endereco'),
    
]
