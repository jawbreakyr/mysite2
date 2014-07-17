from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth import models



from polls.models import Choice, Poll

# from django.template import RequestContext, loader

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


class ResultsView(generic.DetailView):
	model = Poll
	template_name = 'polls/results.html'
	

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
	return HttpResponseRedirect(reverse('polls:detail', args=(p.id,)))

# class login(models.User):
# 	username = models.UserNameField(max_length=30)
# 	first_name = models.CharField(max_length=30)
# 	last_name = models.CharField(max_length=30)
# 	template_name = 'polls/login.html'




















def login(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'polls/login.html', c)


def authen_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/polls/loggedin')
	else:
		return HttpResponseRedirect('/polls/invalid')

def loggedin(request):
	return render(request, 'polls/loggedin.html',
		{'full_name': request.user.username})

def invalid_login(request):
	return render(request, 'polls/invalid.html')


def logout(request):
	auth.logout(request)
	return render(request, 'polls/logout.html')


# Create your views here.
