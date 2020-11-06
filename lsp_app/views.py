from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.
import datetime
from .forms import NewPatient, NewLine, NewPlan
from .models import Patient, Line, Plan
from django.db.models import Q

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

def new_line(request):
	#post= get_object_or_404(Line, pk=pk)
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = NewLine(request.POST)
	# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			form.save()
			# redirect to a new URL:
			pass
	# if a GET (or any other method) we'll create a blank form
	else:
		form = NewLine()
		
	return render(request, 'newline.html', {'form': form})

def new_plan(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewPlan(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            pass
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewPlan()

    return render(request, 'newplan.html', {'form': form})

def all_patients(request):
    all_patients= Patient.objects.all()
    all_lines= Line.objects.all()
    
    for patient in all_patients:
        patient_id = patient.id
        # ~ line = Line.objects.filter(patient_id= patient_id)
        #due_date = line.line_name    
  
    context={
    'all_patients' : all_patients,
    'all_lines' : all_lines,
    # ~ 'line' : line
    }
    return render(request, 'dashboard.html', context)

def today_plans(request):
    today_plans= Patient.objects.filter(Q(peg_due_date=datetime.date.today()) or Q(tt_due_date=datetime.date.today()))
    #today_plans= Patient.objects.all()
    context={
    'today_plans' : today_plans
    }
    return render(request, 'dashboard.html', context)


