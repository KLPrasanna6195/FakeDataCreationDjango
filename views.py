from django.shortcuts import render
from dummydata.models import users

# Create your views here.

def users_view(request):
    Users = users.objects.all()
    return render(request,'Testapp/results.html',{'Users':Users})