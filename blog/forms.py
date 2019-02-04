class CommentForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['content',]
