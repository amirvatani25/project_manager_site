from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class customUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
        labels = {
            'first_name':'نام و نام خانوادگی',
            'email':'ادرس ایمیل',
            'username': 'یوزرنیم',
            'password1':'رمز',
            'password2':'تایید رمز'

        }

    def __init__(self, *args, **kwargs):
        super(customUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class': 'input', 'placeholder': 'نام و نام خانوادگی خود را وارد نمایید'})
        self.fields['email'].widget.attrs.update({'class': 'input', 'placeholder': 'ایمیل خود را وارد نمایید'})
        self.fields['username'].widget.attrs.update({'class': 'input', 'placeholder': 'یوزرنیم خود را وارد نمایید'})
        self.fields['password1'].widget.attrs.update({'class': 'input', 'placeholder': 'رمز خود را وارد نمایید'})
        self.fields['password2'].widget.attrs.update({'class': 'input', 'placeholder': 'لطفا دوباره رمز خود را وارد نمایید'})

class profileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','email','username',
        'location','profile_image', 'phone_number']
        labels = {
            'name':'نام',
            'email':'ایمیل',
            'username': 'یوزرنیم',
            'location':'شهر محل زندگی',
            'profile_image':'عکس پروفایل',
            'phone_number':'شماره تلفن'
        }

    def __init__(self, *args, **kwargs):
        super(profileForm, self).__init__(*args, **kwargs)

        for name , field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
