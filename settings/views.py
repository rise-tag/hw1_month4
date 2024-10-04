from django.shortcuts import render

def settings(request): 
    context = {
        "Title": "Байбол",
        "Undertitle": "Это новая страница!"
    }
    return render(request, 'index.html', context)
