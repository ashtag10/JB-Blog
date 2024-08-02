from typing import Any
from django.contrib.auth.forms import UserCreationForm
from .models import BlogUser

class SignupForm(UserCreationForm):
    def __init__(self, *args: Any, **kwargs) -> None:
        super(SignupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control form-control-sm"

    class Meta:
        model=BlogUser
        fields=["first_name", "last_name", "email", "phone", "address", "profile_picture"]