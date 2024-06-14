from django.shortcuts import render
from .models import Student, Reward
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
    students = Student.objects.order_by("-buck_amount")[:15]
    return render(response, "myapp/home.html", {"students":students})

#renders the page with prizes and merchandise that the students can get by redeeming ninja bucks.
def rewards(response):
    reward_list = Reward.objects.all()
    return render(response, "myapp/rewards.html", {"reward_list":reward_list})

def search(response):
    if response.method == "POST":
        searched = response.POST['searched']

        students = Student.objects.filter(first_name__startswith=searched)
        return render(response, "myapp/search.html", {"searched":searched, "students":students})
    else:
        return render(response, "myapp/search.html", {})
