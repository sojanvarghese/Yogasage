from django.shortcuts import render, redirect
from yoga.models import Email, UserDetails
import json
from django.http import JsonResponse

def pwarrior(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_data')

        # Process the image data and make predictions

        # Dummy predictions for demonstration purposes
        predictions = [
            {'className': 'Label 1', 'probability': 0.8},
            {'className': 'Label 2', 'probability': 0.2},
        ]

        return JsonResponse({'predictions': predictions})

    return JsonResponse({'error': 'Invalid request method'})


def home(request):
    if request.method == 'POST':
        email = request.POST['email']
        request.session['email'] = email  # Store email in session
        try:
            Email.objects.get(address=email)
            return redirect('getstarted')
        except Email.DoesNotExist:
            return redirect('details')

    return render(request, 'home.html')

def details(request):
    if request.method == 'POST':
        email = request.session.get('email')  # Retrieve email from session
        if not email:
            return redirect('home')  # Redirect to home page if email is not found in session

        name = request.POST['name']
        age = int(request.POST['age'])
        gender = request.POST['gender']
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])
        bmi = weight / ((height/100) * (height/100))

        user_details = UserDetails.objects.create(name=name, gender=gender, age=age, weight=weight, height=height, bmi=bmi)
        user_details.save()

        try:
            email_obj = Email.objects.get(address=email)
        except Email.DoesNotExist:
            email_obj = Email.objects.create(address=email)

        email_obj.bmi = bmi
        email_obj.save()

        return redirect('getstarted')

    return render(request, 'details.html')

def getstarted(request):
    email = request.session.get('email')
    try:
            email_obj = Email.objects.get(address=email)
    except Email.DoesNotExist:
            email_obj = Email.objects.create(address=email)
    try:
        
        bmi = email_obj.bmi 
        if bmi < 18.5:
            return redirect('uday1')
        elif 18.5 <= bmi < 25:
            return redirect('nday1')
        elif 25<= bmi <500:
            return redirect('oday1')

    except UserDetails.DoesNotExist:
        return render(request, 'details.html')



def uday1(request):
    return render(request, 'uday1.html')

def uday2(request):
    return render(request, 'uday2.html')

def nday1(request):
    return render(request, 'nday1.html')

def nday2(request):
    return render(request, 'nday2.html')

def oday1(request):
    return render(request, 'oday1.html')

def oday2(request):
    return render(request, 'oday2.html')

def treepose(request):
    return render(request, 'treepose.html')
def easy(request):
    return render(request, 'easy.html')
def diamond(request):
    return render(request, 'diamond.html')
def goddess(request):    
    return render(request, 'goddess.html')
def triangle(request):
    return render(request, 'triangle.html')
def warrior(request):
    return render(request, 'warrior.html')
def End(request):
    return render(request, 'End.html')
