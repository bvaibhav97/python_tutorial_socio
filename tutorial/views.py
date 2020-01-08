from django.shortcuts import render
import time
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from tutorial.authhelper import get_signin_url
from django.urls import reverse
from tutorial.outlookservice import get_me, get_my_messages, get_my_events, get_my_contacts
from tutorial.authhelper import get_signin_url, get_token_from_code, get_access_token
#below is app id
#c5fe3b31-beab-4cb7-87f6-ff543c8d6dba

#below is client secret value
#l=.-4ofJ9sCVb?0F5bw5B28NpnB7UY/1
def events(request):
  access_token = get_access_token(request, request.build_absolute_uri(reverse('tutorial:gettoken')))
  # If there is no token in the session, redirect to home
  if not access_token:
    return HttpResponseRedirect(reverse('tutorial:home'))
  else:
    events = get_my_events(access_token)
    context = { 'events': events['value'] }
    return render(request, 'tutorial/events.html', context)

def home(request):
	redirect_uri = request.build_absolute_uri(reverse('tutorial:gettoken'))
	print(redirect_uri)
	sign_in_url = get_signin_url(redirect_uri)
	context = { 'signin_url': sign_in_url }
	return render(request, 'tutorial/home.html', context)

# Add import statement to include new function
def contacts(request):
  access_token = get_access_token(request, request.build_absolute_uri(reverse('tutorial:gettoken')))
  # If there is no token in the session, redirect to home
  if not access_token:
    return HttpResponseRedirect(reverse('tutorial:home'))
  else:
    contacts = get_my_contacts(access_token)
    context = { 'contacts': contacts['value'] }
    return render(request, 'tutorial/contacts.html', context)
def mail(request):
  access_token = get_access_token(request, request.build_absolute_uri(reverse('tutorial:gettoken')))
  # If there is no token in the session, redirect to home
  if not access_token:
    return HttpResponseRedirect(reverse('tutorial:home'))
  else:
    messages = get_my_messages(access_token)
    context = { 'messages': messages['value'] }
    return render(request, 'tutorial/mail.html', context)

def gettoken(request):
  auth_code = request.GET['code']
  redirect_uri = request.build_absolute_uri(reverse('tutorial:gettoken'))
  token = get_token_from_code(auth_code, redirect_uri)
  print("thats token",token)
  access_token = token['access_token']
  user = get_me(access_token)
  refresh_token = token['refresh_token']
  expires_in = token['expires_in']

  # expires_in is in seconds
  # Get current timestamp (seconds since Unix Epoch) and
  # add expires_in to get expiration time
  # Subtract 5 minutes to allow for clock differences
  expiration = int(time.time()) + expires_in - 300

  # Save the token in the session
  request.session['access_token'] = access_token
  request.session['refresh_token'] = refresh_token
  request.session['token_expires'] = expiration
  return HttpResponseRedirect(reverse('tutorial:mail'))