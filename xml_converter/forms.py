from django import forms
from django.core.validators import FileExtensionValidator


class UploadForm(forms.Form):
    file = forms.FileField(
        required=True,
        validators=[FileExtensionValidator(['xml'])]
    )
