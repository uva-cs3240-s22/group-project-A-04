from django import forms

class DeepThoughtForm(forms.Form):
    """Form for submitting deep thoughts."""

    title = forms.CharField(max_length=200)
    text = forms.CharField(widget=forms.Textarea)

    required_css_class = "bootstrap5-req"
    use_required_attribute = False