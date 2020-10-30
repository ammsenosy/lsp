from django import forms
import datetime
from .models import Patient

class NewPatient(forms.Form):
    name = forms.CharField(max_length=300,label='Patient Name')
    mr_no = forms.IntegerField(label='MR No.')
    room_no = forms.IntegerField(label='Room No.')
    Diagnosis = forms.CharField(max_length=300, label='Diagnosis')
    Consultant = forms.ChoiceField(choices=(('AK','Ahmed Elshahat Kabil'),('KH', 'Khaled AlAbdi')))

    today = datetime.date.today()

    tt_is_there = forms.BooleanField(required=True)
    tt_insert_date = forms.DateField(required=True)
    tt_type = forms.ChoiceField(choices=[('TR','Traco'), ('SE','Something Else')], required=True)
    tt_size = forms.DecimalField(max_digits=3, decimal_places=2, required=True)
        

    peg_is_there = forms.BooleanField(required=True)
    peg_insert_date = forms.DateField(required=True)
    peg_size = forms.DecimalField(max_digits=3, decimal_places=2, required=True)


    def save(self):
        #define validity time
        tt_validity= datetime.timedelta(days=90)
        peg_validity= datetime.timedelta(days=180)

        #calculate due dates
        cal_tt_due_date= self.cleaned_data['tt_insert_date'] + tt_validity
        cal_peg_due_date= self.cleaned_data['peg_insert_date'] + peg_validity

        #create the new object
        new_patient= Patient.objects.create(
        name= self.cleaned_data['name'],
        mr_no= self.cleaned_data ['mr_no'],
        room_no= self.cleaned_data ['room_no'],
        Diagnosis= self.cleaned_data ['Diagnosis'],
        tt_is_there= self.cleaned_data ['tt_is_there'],
        tt_insert_date= self.cleaned_data ['tt_insert_date'],
        tt_due_date= cal_tt_due_date,
        tt_type= self.cleaned_data ['tt_type'],
        tt_size= self.cleaned_data ['tt_size'],
        peg_is_there= self.cleaned_data ['peg_is_there'],
        peg_insert_date= self.cleaned_data ['peg_insert_date'],
        peg_due_date= cal_peg_due_date,
        peg_size= self.cleaned_data ['peg_size'],
        )

        return new_patient

        #def disable_date_field(self):
        #    if
