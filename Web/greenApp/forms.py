from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, auth
from django import forms
from django.core.exceptions import ValidationError,ObjectDoesNotExist
class LoginInForm(AuthenticationForm):
    
    username = forms.CharField(max_length=30,min_length=8,error_messages={'required': '請輸入賬號','max_length':'您的賬號輸入過長','min_length':'您的賬號輸入過短'})
    password = forms.CharField(min_length=8,error_messages={'required': '請輸入密碼','min_length':'您的密碼輸入過短'})
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            
            self.user_cache = auth.authenticate(self.request, username=username, password=password)
            if  self.user_cache is None:
                try:
                    check_user_active=User.objects.get(username=username)
                    if not check_user_active.is_active:
                        raise forms.ValidationError('您的賬號還未被激活<br>若是新註冊會員，請到您註冊的的信箱去激活賬號。<br>若是舊會員想激活回您的賬號請聯絡我們 <a href="/inform_us">E-mail</a>',code='inactive')
                except ObjectDoesNotExist:
                    pass
                
                raise forms.ValidationError('請輸入正確的賬號與密碼。<br>注意這賬號與密碼輸入會區分大小寫。',code='inactive')
                    
        return self.cleaned_data        
    class Meta():
        model = User
        fields = ('username', 'password')