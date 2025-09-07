from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama aplikasi' : 'Football Shop',
        'nama': 'Ilham Afuw Ghaniy',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)