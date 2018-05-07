from django import forms

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs = {"class": "form-control", "id": "full_name", "placeholder": "Your full name" }))

    email = forms.EmailField(widget=forms.EmailInput(attrs ={"class": "form-control", "id": "email_input", "placeholder": "Your email" }))

    content = forms.CharField(widget=forms.Textarea(attrs = {"class": "form-control", "id": "message_content", "placeholder": "Your message"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")

        return email