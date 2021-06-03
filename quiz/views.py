from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from nomad import tagger

questions = [
    {
        'question': 'What is love',
        'answers': [{'text': 'Baby dont hurt me'},
                    {'text': 'Dont hurt me'},
                    {'text': 'No more!'}]
    },
    {
        'question': 'Who let the dogs out',
        'answers': [{'text': 'Who'},
                    {'text': 'You'},
                    {'text': 'Me'}]
    },
    {
        'question': 'Who is the president of US and A',
        'answers': [{'text': 'Joe Biden'},
                    {'text': 'Barack Obama'},
                    {'text': 'Joe Mama'}]
    }
]


def home(request):
    print("[DEV] Entered home request")
    custom_tagger = tagger.Tagger('parameter tag')

    # Select only prefixed tags
    nomadTaggedKeys = [key for key in request.POST.keys() if key.startswith('nomad_')]
    nomadTaggedValues = [val for key, val in request.POST.items() if key.startswith('nomad_')]

    fname = ""
    lname = ""
    # Parse form only when derandomized values match original
    # TODO: Switch 123, 456 with derandomizer <-----------------------------------------------------------------
    keyIndex = 0
    for key in nomadTaggedKeys:
        # Remove nomad prefix and display tags that we got
        key_no_prefix = key[len('nomad_'):]
        print("[DEV] " + str(key_no_prefix))
        # Handle our values
        if key_no_prefix == '123':
            fname = nomadTaggedValues[keyIndex]
        elif key_no_prefix == '456':
            lname = nomadTaggedValues[keyIndex]
        keyIndex += 1


    # Create context
    context = {
        'questions': questions,
        'current_name': fname + " " + lname
    }
    # Append nomad prefix tag to vars that we want to randomize and randomize them
    # TODO: Switch 123, 456 with randomizer <-----------------------------------------------------------------
    context['fname'] = 'nomad_123'
    context['lname'] = 'nomad_456'

    responseRegular = render(request, 'quiz/home.html', context)
    return responseRegular


def thankyou(request):
    return render(request, 'quiz/thankyou.html')
