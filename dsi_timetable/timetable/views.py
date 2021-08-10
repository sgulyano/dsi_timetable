from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def home(request):
  t = [str(i)+":00-"+str(i+1)+":00" for i in range(9,17)]
  mon = [(None, None, 1), (None, None, 1), ('DSI200', 'Aj.Sarun', 4), ('DSI200', 'Aj.Sarun', 2), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1)]
  tue = [(None, None, 1), (None, None, 1), ('DSI200', 'Aj.Sarun', 4), ('DSI200', 'Aj.Sarun', 2), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1)]
  wed = [(None, None, 1), (None, None, 1), ('DSI200', 'Aj.Sarun', 4), ('DSI200', 'Aj.Sarun', 2), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1)]
  thu = [(None, None, 1), (None, None, 1), ('DSI200', 'Aj.Sarun', 4), ('DSI200', 'Aj.Sarun', 2), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1)]
  fri = [(None, None, 1), (None, None, 1), ('DSI200', 'Aj.Sarun', 4), ('DSI200', 'Aj.Sarun', 2), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1), (None, None, 1)]
  context = {'time':t, 'days':{'Monday':mon, 'Tuesday':tue, 'Wednesday':wed, 'Thursday':thu, 'Friday':fri}}
  return render(request, 'home.html', context)