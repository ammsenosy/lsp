from django.db import models
import datetime

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=300,default='DEFAULT VALUE', blank=True, null=True)
    mr_no = models.IntegerField(default='DEFAULT VALUE', blank=True, null=True)
    room_no = models.IntegerField(default='DEFAULT VALUE', blank=True, null=True)
    Diagnosis = models.CharField(max_length=300, default='DEFAULT VALUE', blank=True, null=True)
    Consultant = models.CharField(max_length=300, choices=[('AK','Ahmed Elshahat Kabil'),('KH', 'Khaled AlAbdi')], blank=True, null=True)
                                                                                                                                            ## Here we define date border.. today and time to change
    today = datetime.date.today()
    time_to_change_tt = datetime.timedelta(weeks=12)
    time_to_change_peg = datetime.timedelta(weeks=24)
    tt_calculated_due_date = today + time_to_change_tt
    peg_calculated_due_date = today + time_to_change_peg
    ## Here we start to define the lines and their properties
    ## TT tube

    tt_is_there = models.BooleanField(default=False,blank=True, null=False)
    tt_insert_date = models.DateField(default=today, blank=True)
    tt_type = models.CharField(max_length=300, choices=[('TR','Traco'), ('SE','Something Else')], blank=True, null=True)
    tt_size = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    tt_due_date = models.DateField(default=tt_calculated_due_date , blank=True)

    ## PEG tube
    peg_is_there = models.BooleanField(default=False,blank=True, null=False)
    peg_insert_date = models.DateField(default=today, blank=True)
    peg_size = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    peg_due_date = models.DateField(default=peg_calculated_due_date , blank=True)
