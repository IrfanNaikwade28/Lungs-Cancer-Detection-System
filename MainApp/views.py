from pyexpat.errors import messages
from django.shortcuts import render
from flask import redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from . import model_deploy as dp
from LungsCancerDetection import settings
from .models import UserProfile
from django.conf import settings  
from django.contrib import messages  # Import the messages module
from .forms  import RegisterForm
from django.contrib.auth.decorators import login_required
from .forms import LoginForm  # Assuming you have a form for login

alldata = None

def index_view(request):
    return render(request, 'index.html')

def features(request):
    return render(request, 'features.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request,'login.html')

def result_chart(request):
    data =  UserProfile.objects.all() 
    return render(request,'ResultChart.html', {'data' : data})




@login_required
def image_upload_page(request):
    global alldata
    if request.method == 'POST':
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'age': request.POST['age'],
            'gender': request.POST['gender'],
            'email': request.POST['email'],
            'city': request.POST['city'],
            'pincode': request.POST['pincode'],
            'data_image': request.FILES['data_image']
        }
        UserProfile.objects.create(**form_data)
        
        base_dir = settings.BASE_DIR
        filename = request.FILES['data_image'].name  
        finalPath = f"{base_dir}/media/{filename}"  
        unstabilizedArr = dp.predictDataUpload(finalPath)[0][0]
        unstabilizedArr = [element * 10 for element in unstabilizedArr]
        orgVar = unstabilizedArr

        # Standard Values
        mynewArray = []
        # stdValue = [0.23036479949951172, 0.032485409174114466, 0.04137823358178139, 0.003039872390218079, 0.07982049137353897, 0.07442216854542494, 0.12846914120018482, 0.011804692912846804, 0.6943830102682114, 0.3424488380551338, 0.5372605845332146, 0.2708531357347965, 0.013331694062799215, 0.08636332117021084]
        # for i,j in zip(stdValue,orgVar):
        #     val = i-j
        #     mynewArray.append(val)
        
        # print(mynewArray)
        
        # unstabilizedArr = mynewArray
        labels = ['Atelectasis', 'Cardiomegaly', 'Consolidation', 'Edema', 'Effusion',
                  'Emphysema', 'Fibrosis', 'Hernia', 'Infiltration', 'Mass', 'Nodule',
                  'Pleural_Thickening', 'Pneumonia', 'Pneumothorax']
        prams = {
            'data1': unstabilizedArr[0],
            'data2': unstabilizedArr[1],
            'data3': unstabilizedArr[2],
            'data4': unstabilizedArr[3],
            'data5': unstabilizedArr[4],
            'data6': unstabilizedArr[5],
            'data7': unstabilizedArr[6],
            'data8': unstabilizedArr[7],
            'data9': unstabilizedArr[8],
            'data10': unstabilizedArr[9],
            'data11': unstabilizedArr[10],
            'data12': unstabilizedArr[11],
            'data13': unstabilizedArr[12],
            'data14': unstabilizedArr[13],
            'lb1': labels[0],
            'lb2': labels[1],
            'lb3': labels[2],
            'lb4': labels[3],
            'lb5': labels[4],
            'lb6': labels[5],
            'lb7': labels[6],
            'lb8': labels[7],
            'lb9': labels[8],
            'lb10': labels[9],
            'lb11': labels[10],
            'lb12': labels[11],
            'lb13': labels[12],
            'lb14': labels[13],
            'form_data' : form_data,
        }
        alldata = prams
        return render(request, 'ResultChart.html', prams,)
        
    else:
        return render(request, 'image_upload_page.html')



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm  # Assuming you have a form for login

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index_view')  # Redirect to the index view upon successful login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()  # Instantiate the form

    return render(request, 'login.html', {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('index_view')

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index_view')  # Redirect to the index view upon successful registration
    else:
        form = RegisterForm()  # Instantiate the form

    return render(request, 'signup.html', {"form": form})




def report(request):
    global alldata
    data = [0.63, 0.64, 0.68, 0.74, 0.7, 0.6, 0.61, 0.65, 0.61, 0.61, 0.55, 0.6, 0.63, 0.62]

    values_list = [value for key, value in alldata.items() if key.startswith('data')]

    result_list = ["Positive" if data_value < values_list[index] else "Negative" for index, data_value in enumerate(data)]
    
    print(alldata)
    return render(request, 'Report.html', {'alldata': alldata, 'result_list': result_list})

