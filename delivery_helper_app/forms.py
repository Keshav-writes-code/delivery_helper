from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import user_types, Profile
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ModelChoiceField(
        queryset=user_types.objects.all(), empty_label="Select User Type", required=True
    )
    partner_id = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ("email", "password1", "user_type", "partner_id")

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
                partner_id=self.cleaned_data["partner_id"],
            )
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove password2 field completely
        if "password2" in self.fields:
            del self.fields["password2"]

    def clean(self):
        # Skip password2 validation
        cleaned_data = super().clean()
        user_type = cleaned_data.get("user_type")
        partner_id = cleaned_data.get("partner_id")

        # Both fields are guaranteed to be cleaned and available
        if user_type and user_type.id == 2:
            if not partner_id or not partner_id.strip():
                self.add_error(
                    "partner_id", "Partner ID is required for delivery agents."
                )

        return cleaned_data
