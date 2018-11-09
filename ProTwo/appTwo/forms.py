from django import forms
from appTwo.models import User

class NewUserForm(forms.ModelForm):#model sınıfından kalıtım aldık.
    class Meta():
        model = User # model: Form oluşturmak için kullanılacak model sınıfı
        fields = '__all__' # fields: Forma eklenecek alanların listesi
