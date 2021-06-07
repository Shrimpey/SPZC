from django.shortcuts import render

from nomad.tagger import Tagger

chosenName = "None"
chosenFood = "None"
chosenColor = "None"
chosenDate = "None"
chosenNumber = "None"


def home(request):

    Tagger.add_param_to_randomize(param_types=['name', 'id'], value='fname')

    chosenName = request.POST.get('fname', 'None') + " " + request.POST.get('lname', 'None')
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
