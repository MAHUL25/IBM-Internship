from django.shortcuts import render
from .FraudDetection import *

# Create your views here.
def index(request):
    return render(request, 'CreditCard/homepage.html', {
        'value': 'Credit Card Fraud Detection',
    })

def Theform(request):
    if request.method == "POST":
        time = request.POST['timeInSecs']
        amount = request.POST['amount']
        acount_number = request.POST['accountNumber']
        card_number = request.POST['creditCardNumber']
        cvv = request.POST['creditCardCVV']
        doe = request.POST['creditCardExpiry']
        credit_score = request.POST['creditScore']

        output = predictData(time, amount, acount_number, card_number, cvv, doe, credit_score)

        if output[0] == 1:
            return render(request, 'CreditCard/homepage.html', {
                'value': 'Fraud Detected',
            })
        else:
            return render(request, 'CreditCard/homepage.html', {
                'value': 'Safe Transaction',
            })

    return render(request, 'CreditCard/formpage.html')

def LoginPage(request):
    return render(request, 'CreditCard/loginpage.html')

def RegisterPage(request):
    return render(request, 'CreditCard/registerpage.html')