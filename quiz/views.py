from django.shortcuts import render

from nomad.tagger import Tagger

chosenName = "None"
chosenFood = "None"
chosenColor = "None"
chosenDate = "None"
chosenNumber = "None"

def TagElements():
    Tagger.add_param_to_randomize(param_types=['name', 'id'], value='fname')
    Tagger.add_param_to_randomize(param_types=['name', 'id'], value='lname')
    Tagger.add_param_to_randomize(param_types=['name', 'id'], value='pizza')
    Tagger.add_param_to_randomize(param_types=['name', 'id'], value='food')
    Tagger.add_param_to_randomize(param_types=['name', 'id'], value='color')
    Tagger.add_param_to_randomize(param_types=['name', 'id'], value='number')
    Tagger.add_param_to_randomize(param_types=['name', 'id'], value='date')

def home(request):

    TagElements()

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
