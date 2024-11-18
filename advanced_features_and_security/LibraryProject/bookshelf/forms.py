from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, label="Title")
    description = forms.CharField(
        widget=forms.Textarea, label="Description", required=False
    )
    published_date = forms.DateField(
        widget=forms.SelectDateWidget, label="Published Date", required=False
    )

