from django.shortcuts import render
#from django.http import HttpResponse
#from appTwo.models import User
from appTwo.forms import NewUserForm


def index(request):
    return render(request,'appTwo/index.html')

def users(request):

    form = NewUserForm() #NewUserForm classını form nesnesine içerik olarak gönderdik.

    if request.method == "POST":
        form = NewUserForm(request.POST) #gelen veriyi form nesnesine attık


        if form.is_valid(): #eğer form isteği doğru gelmişse
            form.save(commit=True)
            return index(request)
        else:
            print('Error Form İnvalid ')

    return render(request,'appTwo/users.html',{'form':form})



    #Bunlar yerine direk formda bilgi göndericez
    #user_list=User.objects.order_by('first_name')#first_name alanına göre sıralanmış verileri user_list'e atıyoruz
    #user_dict={'users':'user_list'}#olusturduğumuz listeyi user_dict' e value olarak attık
    #return render(request,'appTwo/users.html',context=user_dict)
