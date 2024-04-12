from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student
#import csv
#import pandas as pd

# Create your views here.

#renders the leaderboard 'homepage'
def home(response):
    """
    Run only if there are no Students in the database and we have the exported excel sheet of all
    student information. It will, however, set all ninja bucks back to zero.
    with open('myapp/name_of_file.csv') as file:
        # Create reader object by passing the file
        # object to DictReader method
        reader = csv.DictReader(file)

        # Iterate over each row in the csv file
        # using reader object
        for row in reader:
            s = Student(first_name=row['Participant First Name'],
                            last_name=row['Participant Last Name'],
                            buck_amount=0,
                            belt=row['Rank'])
            s.save()
            """
    students = Student.objects.all()
    return render(response, "myapp/home.html", {"students":students})

#renders the page with prizes and merchandise that the students can get by redeeming ninja bucks.
def prizes(response):
    return render(response, "myapp/prizes.html", {})
