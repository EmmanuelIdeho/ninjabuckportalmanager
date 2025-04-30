from django.shortcuts import render
from django.db.models import Q
from .models import Student, Reward

# Create your views here.

#renders the leaderboard
def home(response):
    students = Student.objects.order_by("-buck_amount")[:8]
    return render(response, "myapp/home.html", {"students":students})

#renders the page with prizes and merchandise that the students can get by redeeming ninja bucks.
def rewards(response):
    reward_list = Reward.objects.order_by("-price")
    return render(response, "myapp/rewards.html", {"reward_list":reward_list})

def search(response):
    if response.method == "POST":
        searched = response.POST['searched']
        if searched.strip() == '':
            return render(response, "myapp/search.html", {})

        students = Student.objects.filter(
            Q(first_name__istartswith=searched) | Q(last_name__istartswith=searched)
            )
        return render(response, "myapp/search.html", {"searched":searched, "students":students})
    else:
        return render(response, "myapp/search.html", {})
