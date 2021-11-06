from django.forms import ModelForm
from app.models import Cadastro
from app.models import Contato

# Create the form class.
class CadastroForm(ModelForm):
     class Meta:
         model = Cadastro
         fields = ['situacao', 'nome', 'raca', 'descricao', 'local', 'info', 'telefone', 'email', 'image',]


class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'endereco', 'email', 'telefone', 'descricao', 'image']