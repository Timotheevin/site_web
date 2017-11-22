from django import forms
from .models import User
from django.db import models
from django.core.exceptions import ValidationError

class ConnectionForm(forms.Form):
	name = forms.CharField(max_length=100, label= 'Prénom')
	password = forms.CharField(max_length=100, widget=forms.PasswordInput, label= 'Mot de passe')
	def clean_password(self):
		password = self.cleaned_data['password']
		if "imo" in password:
			raise forms.ValidationError("Eh toi ! Je t'ai vu essayer de te connecter avec mon mot de passe :)")
		return password
	def clean(self):
		cleaned_data = super(ConnectionForm, self).clean()
		name = cleaned_data.get('name')
		password = cleaned_data.get('password')
		if name and password:
			
			password = password.lower()
			name = name.lower()
			if 'é' in password:
				password = password.replace('é','e')
			if 'ç' in password:
				password = password.replace('ç','c')
			if 'é' in name:
				name = name.replace('é','e')
			try:
				user = User.objects.get(password=password)
			except (KeyError, User.DoesNotExist):
				raise forms.ValidationError("Mot de passe invalide")
			else:
				username = user.name
				if username != name:
					raise forms.ValidationError("Identifiant invalide")			
		return cleaned_data
	

class NewmdpForm(forms.Form):
	lastmdp = forms.CharField(max_length=100, label='Ancien mot de passe')
	newmdp = forms.CharField(max_length=100, label='Nouveau mot de passe')
	def clean_lastmdp(self):
		lastmdp = self.cleaned_data['lastmdp']
		try:
			user = User.objects.get(password=lastmdp)
		except (KeyError, User.DoesNotExist):
			raise forms.ValidationError("Mot de passe invalide")
		return lastmdp
'''
id_ = forms.CharField(max_length=100, label="Prénom")
password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
'''
