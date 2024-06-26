from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Введите login', 
        required=True, 
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите login'}
        )
        )
    # some = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(
        label='Введите пароль',
          required=True, 
          help_text='Пароль не должен быть меньше 6 знаков',
          widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
          )
    password2 = forms.CharField(
        label='Подтвердите пароль',
          required=True,
          widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторно введите пароль'})
          )
    email = forms.EmailField(
        label='Введите Email', 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'}
        ))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']


# from django.contrib.auth.forms import UserCreationForm

# class UserRegisterForm(forms.Form):
# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField(label='Введите email', required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2', 'email']

    
