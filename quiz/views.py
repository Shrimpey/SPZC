from django.shortcuts import render

from nomad.tagger import Tagger
#
# chosen_name = "None"
# chosen_food = "None"
# chosen_color = "None"
# chosen_date = "None"
# chosen_number = "None"


def tag_elements():
    Tagger.add_param_to_randomize(param_types=['name', 'id'], value='fname')
    Tagger.add_param_to_randomize(param_types=['name', 'id'], value='lname')
    Tagger.add_param_to_randomize(param_types=['name', 'id'], value='pizza')
    Tagger.add_param_to_randomize(param_types=['name', 'id'], value='food')
    Tagger.add_param_to_randomize(param_types=['name', 'id'], value='color')
    Tagger.add_param_to_randomize(param_types=['name', 'id'], value='number')
    Tagger.add_param_to_randomize(param_types=['name', 'id'], value='date')


def home(request):

    #tag_elements()

    chosen_name = request.POST.get('fname', 'None') + " " + request.POST.get('lname', 'None')
    chosen_food = request.POST.get('food', 'None')
    chosen_color = request.POST.get('color', 'None')
    chosen_date = request.POST.get('date', 'None')
    chosen_number = request.POST.get('number', 'None')

    context = {
        'current_name': chosen_name,
        'current_food': chosen_food,
        'current_options': chosen_color + ", " + chosen_date + ", " + chosen_number,
    }
    return render(request, 'quiz/home.html', context)


def thankyou(request):
    return render(request, 'quiz/thankyou.html')
