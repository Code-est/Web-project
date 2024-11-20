from django import forms
from django.contrib.auth import get_user_model
from .models import Task
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {"title" : TextInput(attrs={
            "class" : "form-control",
            "placeholder": "Введите название"
        }),
            "task" : Textarea(attrs={
            "class" : "form-control",
            "placeholder": "Введите описание"
        }),
        }

class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль", widget = forms.PasswordInput())
    password2 = forms.CharField(label="Повторный пароль", widget = forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name", "password", "password2"]
        labels = {
            "email": "E-mail",
            "first_name": "Имя",
            "last_name": "Фамилия",
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Пароли не совпадают")
        return cd["password"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой Email уже занят")
        return email