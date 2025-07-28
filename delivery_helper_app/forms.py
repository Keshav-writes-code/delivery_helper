from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import user_types, Profile
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ModelChoiceField(
        queryset=user_types.objects.all(), empty_label="Select User Type", required=True
    )

    class Meta:
        model = User
        fields = ("email", "password1", "user_type")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():  # YOUR custom check
            raise forms.ValidationError("Email already registered")

        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]

        if commit:
            user.save()
            Profile.objects.create(
                auth_user=user,
                user_type_id=self.cleaned_data["user_type"],
                partner_id="",
            )
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove password2 field completely
        if "password2" in self.fields:
            del self.fields["password2"]

    def clean(self):
        # Skip password2 validation
        cleaned_data = self.cleaned_data
        return cleaned_data
