from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import User


class LoginForm(forms.Form):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput,
        label="Email"
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput,
        label="Password"
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.label_class = "font-weight-bold"
        self.helper.form_error_title = "Oops"
        self.helper.add_input(
            Submit('login', 'Login', css_class="btn-block")
        )
