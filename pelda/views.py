from django.shortcuts import render, redirect
from .models import Termek
from .forms import TermekForm
from django.http import HttpResponse

# Create your views here.
def termekek_nezet(request):
    termekek = Termek.objects.all()
    return render(request, 'termekek.html', {'termekek': termekek})

def uj_termek(request):
    if request.method == 'GET':
        form = TermekForm()
        return render(request, 'uj-termek.html', {'urlap': form})
    elif request.method == 'POST':
        form = TermekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('termekek')
        else:
            return HttpResponse('<h1> Hoppsz! Ez nem sikerült, probálja újra. </h1>')