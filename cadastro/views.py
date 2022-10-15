from django.shortcuts import render
from django.utils.crypto import get_random_string
from .models import Usuario

# Create your views here.
def cadastro(request):
    err_name : bool = False
    err_date : bool = False
    success : bool = False
    if request.method == 'POST':
        usuario = Usuario(
            usuario=request.POST['usuario'],
            senha=request.POST['senha'],
            nasc=request.POST['nasc']
            )
        
        if getattr(usuario, 'usuario') == '':
            err_name = True
        if getattr(usuario, 'nasc') == '':
            err_date = True
        
        if getattr(usuario, 'senha') == '':
            setattr(usuario, 'senha', get_random_string(12))
        
        if err_name == False and err_date == False:
            usuario.save()
            success = True
        
    return render(request, 'index.html', {'errName': err_name, 'errDate': err_date, 'success': success})