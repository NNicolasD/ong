from .models import Usuario
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm


class RegistroUsuarioForm(UserCreationForm):

    class Meta:
        model  = Usuario
        fields = ['username','password1','password2']
        help_text = {k:"" for k in fields}

    @transaction.atomic
    def save(self):
        user              = super().save(commit=False)
        user.is_superuser = False
        user.is_staff     = False
        user.save()
        return user