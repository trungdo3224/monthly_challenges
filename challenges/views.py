from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here

monthly_challenges = {
  "january": "Eat no meat",
  "february": "Walk 15 minutes every day",
  "march": "March challenge",
  "april": "April challenge",
  "may": "May challenge",
  "june": "June challenge",
  "july": "July challenge",
  "august": "August challenge",
  "september": "September challenge",
  "october": "October challenge",
  "november": "November challenge",
  "december": "December challenge"
}

def index(request):
  list_items = ""
  months = list(monthly_challenges.keys())

  for month in months:
    capitialized_month = month.capitalize()
    month_path = reverse("month-challenge", args=[month])
    list_items += f"<h2><li><a href=\"{month_path}\">{capitialized_month}</li></h2>"
  response_data = f"<ul>{list_items}</ul>"
  return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())
  if month <= 0 or month > len(months):
    return HttpResponseNotFound("This month is not supported!")
  else:
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
  return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    response_data = f"<h1>{challenge_text}</h1>"
    return HttpResponse(response_data)
  except:
    return HttpResponseNotFound("<h1>This month is not supported!</h1>")