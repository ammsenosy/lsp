from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

from .forms import NewPatient
from .models import Patient


def get_patient(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewPatient(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            pass
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewPatient()

    return render(request, 'newpatient.html', {'form': form})

def all_patients(request):
    all_patients= Patient.objects.all()
    context={
    'all_patients' : all_patients
    }
    return render(request, 'dashboard.html', context)

def today_plans(request):
    today_plans= Patient.objects.filter(Q(peg_due_date=datetime.date.today()) or Q(tt_due_date=datetime.date.today()))
    #today_plans= Patient.objects.all()
    context={
    'today_plans' : today_plans
    }
    return render(request, 'dashboard.html', context)
