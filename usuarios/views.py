from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from usuarios.forms import LoginForm, CadastroForm

def login(request):
    form = LoginForm()

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForm()

    if request.method == 'POST':
        form = CadastroForm(request.POST)
        
        if form.is_valid():
            if form['senha'].value() != form['confirmar_senha'].value():
                return redirect('cadastro')

            nome = form['nome_login'].value()
            email = form['email'].value()
            senha = form['senha'].value()
            
            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')
            
            usuario = User.objects.create_user(username=nome, email=email, password=senha)

            usuario.save()

            return redirect('login')

        
    return render(request, 'usuarios/cadastro.html', {'form': form})