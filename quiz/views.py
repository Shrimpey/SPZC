from django.shortcuts import render


chosenName = "None"
chosenFood = "None"
chosenColor = "None"
chosenDate = "None"
chosenNumber = "None"


def home(request):

    chosenName = request.POST.get('__RaNmE__fname', 'None') + " " + request.POST.get('lname', 'None')
    chosenFood = request.POST.get('food', 'None')
    chosenColor = request.POST.get('color', 'None')
    chosenDate = request.POST.get('date', 'None')
    chosenNumber = request.POST.get('number', 'None')

    context = {
        'current_name': chosenName,
        'current_food': chosenFood,
        'current_options': chosenColor + ", " + chosenDate + ", " + chosenNumber,
    }
    return render(request, 'quiz/home.html', context)


def thankyou(request):
    return render(request, 'quiz/thankyou.html')
