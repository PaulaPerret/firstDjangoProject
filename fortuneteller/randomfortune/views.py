from django.shortcuts import render
import random

# Create your views here.
fortuneList = [
    "Today is a good day to wear blue",
    "You should drink more apple juice",
    "You are getting that job soon",
    "You should trust yourself more",
    "Eat healthier food is gonna make you feel better"
]
horoscopeList = [
    "If you want to succed work hard",
    "You are going to have a romantic date this week",
    "This is a good week to spend time with friends and family",
    "Blue is your lucky color",
    "Your lucky number for this week is 13"
]
def fortune(request):
    horoscope = random.choice(horoscopeList)
    fortune = random.choice(fortuneList)
    context = {"fortune": fortune, "horoscope": horoscope}
    return render(request,'randomfortune/fortune.html', context)
  
