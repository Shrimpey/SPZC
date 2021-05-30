from django.shortcuts import render


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
    context = {
        'questions': questions
    }
    return render(request, 'quiz/home.html', context)


def thankyou(request):
    return render(request, 'quiz/thankyou.html')
