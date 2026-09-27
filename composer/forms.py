from django import forms

class EmailForm(forms.Form):
    from_local_part = forms.CharField(label="From (local part)")
    reply_to = forms.EmailField(label="Reply-To", required=False)
    to = forms.CharField(help_text="Comma-separated addresses")
    cc = forms.CharField(required=False)
    bcc = forms.CharField(required=False)
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField(required=False)