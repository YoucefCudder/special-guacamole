from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)

    def save(self):
        if self.is_valid():
            print("Form is valid")
            print("First name: " + self.cleaned_data["first_name"])
            print("Last name: " + self.cleaned_data["last_name"])
            print("Email address: " + self.cleaned_data["email_address"])
            print("Message: " + self.cleaned_data["message"])
        else:
            print("Form is invalid")


