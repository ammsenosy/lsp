from django.db import models
import datetime


# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=30,default='DEFAULT VALUE', blank=False, null=False)
    mr_no = models.IntegerField(blank=False, null=False)
    tt_is_there = models.BooleanField(default=False,blank=True, null=False)

    def __str__(self):
        return self.name


#    Consultant = models.CharField(max_length=300, choices=[('AK','Ahmed Elshahat Kabil'),('KH', 'Khaled AlAbdi')], blank=True, null=True)
'''                                                                                                                                            ## Here we define date border.. today and time to change
    today = datetime.date.today()
    time_to_change_tt = datetime.timedelta(weeks=12)
    time_to_change_peg = datetime.timedelta(weeks=24)
    tt_calculated_due_date = today + time_to_change_tt
    peg_calculated_due_date = today + time_to_change_peg
    ## Here we start to define the lines and their properties
    ## TT tube


    ## PEG tube

    peg_is_there = models.BooleanField(default=False,blank=True, null=False)
    peg_insert_date = models.DateField(default=today, blank=True)
    peg_size = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    peg_due_date = models.DateField(default=peg_calculated_due_date , blank=True)
'''

class Plan(models.Model):
    patient= models.ManyToManyField(Patient)
    line_name= models.CharField(max_length=30,default='DEFAULT VALUE', blank=False, null=False)
    plan_name= models.CharField(max_length=30,default='DEFAULT VALUE', blank=False, null=False)
    time= models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.line_name


class Line(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    line_name = models.ForeignKey(Plan, on_delete=models.CASCADE)
    insert_date = models.DateField(blank=False, null=False)
    type = models.CharField(max_length=30, blank=True, null=True)
    size = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    due_date = models.DateField(blank=False, null=False)
    removal_date= models.DateField(blank=True, null=True)

    def __str__(self):
        return self.line_name
