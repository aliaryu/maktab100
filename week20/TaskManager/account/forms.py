from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class LoginForm(AuthenticationForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'password',]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control fw-custom',
            'id': 'username',
            'name': 'username',
            'placeholder': "Enter Username",
            'required': True,
        })

        self.fields['password'].widget.attrs.update({
            'type': 'password',
            'class': 'form-control fw-custom',
            'id': 'password',
            'name': 'password',
            'placeholder': "Enter Password",
            'required': True,
        })
