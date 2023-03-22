from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        
        fields = ['email','city','state','fullname','gender','visiblity','password1','password2','profile_image']
        

    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.extra_field = self.cleaned_data["extra_field"]
    #     if commit:
    #         user.save()
    #     return user