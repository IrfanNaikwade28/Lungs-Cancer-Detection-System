from pyexpat.errors import messages
from django.shortcuts import render
from flask import redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from MainApp.forms import SignUpForm
from . import model_deploy as dp
from LungsCancerDetection import settings
from .models import UserProfile
from django.conf import settings  
from django.contrib import messages  # Import the messages module
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


def image_upload_page(request):
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
        return render(request, 'ResultChart.html', prams,)
    else:
        return render(request, 'image_upload_page.html')



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login(request, user)
            messages.success(request, 'You have been logged in successfully')
            return redirect('image_upload_page')
        else:
            messages.error(request, "Username or Password is incorrect !!")  # Use messages.error for warning/error messages
            return redirect('login_user')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('index_view')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('index_view')
        else:
            form = SignUpForm(request.POST)
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)