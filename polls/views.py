from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
# from django.views.generic.edit import FormView


from polls.models import Choice, Poll
from polls.forms import MyRegistrationForm
from polls.forms import AuthenForm



# views using generic CBV
class HomeView(generic.TemplateView):
	template_name = 'polls/home.html'


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_poll_list'

	def get_queryset(self):
		""" Return the last five published polls. """
		return Poll.objects.order_by('-pub_date')[:]
	

class DetailView(generic.DetailView):
	model = Poll
	template_name = 'polls/detail.html'


"""Disabled the ResultsView class as it was no longer 
   needer as the result was already tagged along with 
   the DetailView"""
# class ResultsView(generic.DetailView):
# 	model = Poll
# 	template_name = 'polls/results.html'
	

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# redisplay the poll voting form.
		return render(request, 'polls/detail.html', {
			'poll': p,
			'error_message': "Pick a choice you fuck'n idiot!",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after succesfully dealing
		# with POST data. This prevents from being posterd twice if a
		# use hits the Back button.
	return redirect('polls:detail', p.id)



def login(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'polls/login.html', c)


# class AuthenView(generic.TemplateView):
# 	template_name = 'polls/login.html'

# 	def get(self, request, *args, **kwargs):
# 		context = {"forms": AuthenForm()}
# 		return self.render_to_response(context)

# 	def post(self, request, *args, **kwargs):
# 		forms = AuthenForm(request.POST)
# 		if forms.is_valid():
# 			forms.save()
# 			return redirect("polls:loggedin")
# 		context = {"forms": forms}
# 		return self.render_to_response(context)




def authen_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return redirect('polls:loggedin')
	else:
		return redirect('polls:invalid')
	

def loggedin(request):
	return render(request, 'polls/loggedin.html',
		{'full_name': request.user.username})

def invalid_login(request):
	return render(request, 'polls/invalid.html')


def logout(request):
	auth.logout(request)
	return render(request, 'polls/logout.html')

# class ContactView(FormView):
# 	template_name = 'polls/register.html'
# 	form_class = ContactForm
# 	success_url = '/thanks/'

# 	def form_valid(self, form):
# 		# This method is called when valid form data has been POSTed
# 		# It should return an HttpResponse
# 		form.send_email()
# 		return super(ContactView, self).form_valid(form)

	# def register_user(request):
	# 	if request.method == 'POST':
	# 		form = MyRegistrationForm(request.POST)
	# 		if form.is_valid():
	# 			form.save()
	# 			return redirect('/polls/register_success')

# 	args = {}
# 	args.update(csrf(request))

# 	args['form'] = MyRegistrationForm()
# 	print args
# 	return render(request, 'polls/register.html', args)

class RegisterView(generic.TemplateView):
	"""
	a far more better view using generic CVB
	"""
	template_name = "polls/register.html"

	def get(self, request, *args, **kwargs):
		context = {"form": MyRegistrationForm()}
		return self.render_to_response(context)

	def post(self, request, *args, **kwargs):
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("polls:register_success")
		context = {"form": form}
		return self.render_to_response(context)


def register_success(request):
	return render(request, 'polls/register_success.html')
# Create your views here.
