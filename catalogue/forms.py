# django imports
from django import forms
from canleath.validators import NAME_VALIDATOR, MobileNumberValidator
from .models import NewsLetter

class ContactUsForm(forms.Form):
    """
    contact us form
    """

    first_name = forms.CharField(
        max_length=50,
        required=True,
        validators=[
            NAME_VALIDATOR,
        ],
        widget=forms.TextInput(attrs={'data-constraints': '@Required', 'class': 'form-control', 'placeholder':'First Name',},)
    )

    last_name = forms.CharField(
        max_length=50,
        required=True,
        validators=[
            NAME_VALIDATOR,
        ],
        widget=forms.TextInput(attrs={'data-constraints': '@Required', 'class': 'form-control', 'placeholder':'Last Name',},)
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'data-constraints': '@Email @Required', 'class': 'form-control', 'placeholder':'Email', },)
    )

    phone = forms.CharField(
        max_length=10,
        validators=[
            MobileNumberValidator,
        ],
        widget=forms.TextInput(attrs={'data-constraints': '@Numeric', 'class': 'form-control', 'placeholder':'Phone', 'maxlength':'10','oninput':"this.value=this.value.replace(/[^0-9]/g,'');"},)
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'data-constraints': '@Required', 'class': 'form-control form-control-has-validation form-control-last-child', 'placeholder':'Message'}, ),
    )


class NewsLetterForm(forms.ModelForm):
    """
    News Letter form
    """

    email = forms.EmailField(widget=forms.EmailInput(attrs={'data-constraints': '@Email @Required', 'class': 'form-input',}))

    def clean_email(self):
        data = self.cleaned_data.get('email')
        if NewsLetter.objects.filter(email=data).exists():
            raise forms.ValidationError('A User With this Email is already Subscribed')
        return data

    class Meta:
        model = NewsLetter
        fields = (
            'email',
        )