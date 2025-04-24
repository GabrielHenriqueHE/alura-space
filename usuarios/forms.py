from django import forms


class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ex.: João Silva"}
        ),
    )

    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Digite sua senha"}
        ),
    )


class CadastroForm(forms.Form):
    nome_login = forms.CharField(
        label="Nome de login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ex.: João Silva"}
        ),
    )

    email = forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Ex.: joaosilva@xpto.com"}
        ),
    )

    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Digite sua senha"}
        ),
    )

    confirmar_senha = forms.CharField(
        label="Confirmação de senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Digite sua senha novamente"}
        ),
    )

    def clean_nome_login(self):
        nome = self.cleaned_data.get("nome_login")

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError(
                    "Não é possível inserir espaços no nome de login."
                )
            else:
                return nome

    def clean_confirmar_senha(self):
        senha = self.cleaned_data.get("senha")
        confirmar_senha = self.cleaned_data.get("confirmar_senha")

        if senha and confirmar_senha:
            if senha != confirmar_senha:
                raise forms.ValidationError("As senhas não são iguais.")
            else:
                return confirmar_senha
