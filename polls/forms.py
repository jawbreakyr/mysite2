from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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

class AuthenForm(AuthenticationForm):
	username = forms.CharField(max_length=100)
	password = forms.CharField(label=("Password"), widget=forms.PasswordInput)

	error_messages = {
		'invalid_login': ("Please enter a correct %(username)s and password. "
							"Note that both fields may be case-sensitive."),
		'inactive': ("This account is inactive."),
		}

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		try:
			self.user_cache = authenticate(username=username,
				password=password)
			if user_cache is None:
				raise forms.ValidationError(
					self.error_messages['invalid_login'],
					code='invalid_login',
					params={'username': self.username_field.verbose_name},
				)
			elif not self.user_cache.is_active:
				raise forms.ValidationError(
					self.error_messages['inactive'],
					code='inactive',
				)
		except self.user_cache.is_valid:

			return self.cleaned_data







		# if username and password:
		# 	self.user_cache = authenticate(username=username,
		# 		password=password)
		# 	if self.user_cache is None:
		# 		raise forms.ValidationError(
		# 			self.error_messages['invalid_login'],
		# 			code='invalid_login',
		# 			params={'username': self.username_field.verbose_name},
		# 		)
		# 	elif not self.user_cache.is_active:
		# 		raise forms.ValidationError(
		# 			self.error_messages['inactive'],
		# 			code='inactive',
		# 		)
		# return self.cleaned_data

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

