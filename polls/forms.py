from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def clean(self):
		pass1 = self.cleaned_data.get("password1")
		pass2 = self.cleaned_data.get("password2")

		# import pdb; pdb.set_trace()
		
		if pass1 != pass2:
			raise forms.ValidationError("Password doesn't match!")
		return self.cleaned_data

	# def save(self, commit=True):
	# 	user = super(UserCreationForm, self).save(commit=False)
	# 	user.email = self.cleaned_data['email']

	# 	if commit:
	# 		user.save()

	# 	return user



# class ContactForm(forms.Form):
# 	name = forms.CharField()
# 	message = forms.CharField(widget=forms.Textarea)

# 	def send_email(self):
# 		# send email using the self.cleaned_data dictionary
# 		pass

