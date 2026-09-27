from django import forms

class EmailForm(forms.Form):
    from_local_part = forms.CharField(label="From (before @kergsdev.site)")
    to = forms.CharField(help_text="Comma-separated addresses")
    cc = forms.CharField(required=False)
    bcc = forms.CharField(required=False)
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)