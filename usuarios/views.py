from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from usuarios.forms import CadastroForm, LoginForm


def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha"].value()

            usuario = auth.authenticate(request, username=nome, password=senha)

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, "Usuário autenticado com sucesso.")

                return redirect("index")
            else:
                messages.error(request, "Credenciais inválidas para autenticação.")

                return redirect("login")

    return render(request, "usuarios/login.html", {"form": form})


def cadastro(request):
    form = CadastroForm()

    if request.method == "POST":
        form = CadastroForm(request.POST)

        if form.is_valid():
            if form["senha"].value() != form["confirmar_senha"].value():
                messages.error(request, "Credenciais inválidas para autenticação.")

                return redirect("cadastro")

            nome = form["nome_login"].value()
            email = form["email"].value()
            senha = form["senha"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Um outro usuário já utiliza esse nome.")

                return redirect("cadastro")

            usuario = User.objects.create_user(
                username=nome, email=email, password=senha
            )

            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso.")

            return redirect("login")

    return render(request, "usuarios/cadastro.html", {"form": form})


def logout(request):
    messages.success(request, "Logout efetuado.")
    auth.logout(request)
    return redirect("index")
