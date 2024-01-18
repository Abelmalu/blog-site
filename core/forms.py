from django import forms
from. import models
class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields=['title','body','slug','thumb']




class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['first_name','last_name','profile_pic']