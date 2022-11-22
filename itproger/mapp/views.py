from django.shortcuts import render


def index(request):
    data = {
        'title': 'Новый тайтл для главной',
        'values' : ['Василий','Сергей','Александр','Петя'],
        'obj' : {
            'car': 'Subaru',
            'Age': 46,
            'Hobby':'Development'
        }
    }
    return render(request, 'mapp/index.html', data )


def about(request):
    return render(request, 'mapp/about.html')
