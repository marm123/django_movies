from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, UserCreationForm
)
from django.db.transaction import atomic
from django.forms import CharField, Form, Textarea, IntegerField

from accounts.models import Profile

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
    shoe_size = IntegerField(
        label = 'Your shoe size',
        min_value=28, max_value=54
    )

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    def save(self, commit=True, *args, **kwargs):
        user = super().save(commit)
        shoe_size = self.cleaned_data['shoe_size']
        profile = Profile(shoe_size=shoe_size, user=user)
        profile.save()
        return user
