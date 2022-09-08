from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Eat no meat for entire month!",
    "february": "Walk for atleast 20min everyday",
    "march": "Learn Django for atleast 20min everyday",
    "april": "Eat no meat for entire month!",
    "may": "Walk for atleast 20min everyday",
    "june": "Learn Django for atleast 20min everyday",
    "july": "Eat no meat for entire month!",
    "august": "Walk for atleast 20min everyday",
    "september": "Learn Django for atleast 20min everyday",
    "october": "Eat no meat for entire month!",
    "november": "Walk for atleast 20min everyday",
    "december": "Learn Django for atleast 20min everyday",
}

# Create your views.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
