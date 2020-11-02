from django import forms
import datetime
from .models import Patient, Line, Plan

today = datetime.date.today()

class NewPatient(forms.Form):
    name = forms.CharField(max_length=30,label='Patient Name')
    mr_no = forms.IntegerField(label='MR No.')
#    room_no = forms.IntegerField(label='Room No.')
#    Diagnosis = forms.CharField(max_length=300, label='Diagnosis')
#    Consultant = forms.ChoiceField(choices=(('AK','Ahmed Elshahat Kabil'),('KH', 'Khaled AlAbdi')))

    tt_is_there = forms.BooleanField(required=True)

#    peg_is_there = forms.BooleanField(required=True)
#    peg_insert_date = forms.DateField(required=True)
#    peg_size = forms.DecimalField(max_digits=3, decimal_places=2, required=True)


    def save(self):

        #create the new object
        new_patient= Patient.objects.create(
        name= self.cleaned_data['name'],
        mr_no= self.cleaned_data ['mr_no'],
        tt_is_there= self.cleaned_data ['tt_is_there'],
#        peg_is_there= self.cleaned_data ['peg_is_there'],
#        peg_insert_date= self.cleaned_data ['peg_insert_date'],
#        peg_due_date= cal_peg_due_date,
#        peg_size= self.cleaned_data ['peg_size'],
        )

        return new_patient


class NewPlan(forms.Form):
	line_name= forms.CharField(max_length=30,label='The line/Tube:')
	plan_name= forms.CharField(max_length=30,label='Plan name:')
	time= forms.IntegerField(label='Time to do (in days):')
	
	def save(self):
		new_plan= Plan.objects.create(
		line_name= self.cleaned_data ['line_name'],
		plan_name= self.cleaned_data ['plan_name'],
		time= self.cleaned_data ['time']
		)
		return new_plan


class NewLine(forms.Form):
    TT_TYPES_CHOICES = (
    ('TR', 'Trachoa'),
    ('BR', 'Bourtex'),
    ('CH', 'Chilly')
)
    line_name= forms.ModelChoiceField(queryset=Plan.objects, to_field_name="line_name")
    insert_date = forms.DateField(required=True)
    type = forms.ChoiceField(required=True, choices=TT_TYPES_CHOICES)
    size = forms.DecimalField(max_digits=3, decimal_places=2, required=True)
    patient_name = forms.ModelChoiceField(queryset=Patient.objects, to_field_name="name")

    def save(self):
        #define validity time
        validity= datetime.timedelta(days=90)
#        peg_validity= datetime.timedelta(days=180)

        #calculate due dates
        cal_due_date= self.cleaned_data['insert_date'] + validity
#        cal_peg_due_date= self.cleaned_data['peg_insert_date'] + peg_validity

        #create the new record
        new_line= Line.objects.create(
        line_name= self.cleaned_data ['line_name'],
        insert_date= self.cleaned_data ['insert_date'],
        due_date= cal_due_date,
        type= self.cleaned_data ['type'],
        size= self.cleaned_data ['size'],
        )
        return new_line
