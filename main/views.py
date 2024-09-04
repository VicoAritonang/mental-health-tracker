from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2306219083',
        'name': 'Vico Winner Sebastian Aritonang',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
# Create your views here.
