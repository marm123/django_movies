from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, UserCreationForm
)
from django.db.transaction import atomic
from django.forms import CharField, Form, Textarea

# from accounts.models import Profile


class SubmittableForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(*self.fields, Submit('submit', 'Submit'))


class SubmittableAuthenticationForm(SubmittableForm, AuthenticationForm):
    pass


class SubmittablePasswordChangeForm(SubmittableForm, PasswordChangeForm):
    pass


class SignUpForm(SubmittableForm, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']