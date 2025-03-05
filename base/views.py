from django.shortcuts import render

# Create your views here.


rooms=[
    {'id': 1, 'name': 'Let\'s Chat'},
    {'id': 2, 'name':'Graphics Design'},    
    {'id': 3, 'name':'Doctors'}
]
def home(request):
    context={'rooms':rooms}
    return render(request, 'base/home.html',context)

def room(request,pk):
    room=None
    for i in rooms:
        if i['id']==pk:
            room=i
    context={'room':room}
    return render(request, 'base/room.html')
