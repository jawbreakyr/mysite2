from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import auth
from django.core.context_processors import csrf


from polls.models import Choice, Poll

# from django.template import RequestContext, loader

class HomeView(generic.TemplateView):
	template_name = 'polls/home.html'


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_poll_list'

	def get_queryset(self):
		""" Return the last five published polls. """
		return Poll.objects.order_by('-pub_date')[:5]
	

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
			'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after succesfully dealing
		# with POST data. This prevents from being posterd twice if a
		# use hits the Back button.
	return HttpResponseRedirect(reverse('polls:results', args =(p.id,)))


def login(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'polls/login.html', c)


def authen(request):
	return render(request, 'polls/authen.html')

def logout(request):
	return render(request, 'polls/logout.html')

def loggedin(request):
	return render(request, 'polls/loggedin.html')

def invalid(request):
	return render(request, 'polls/invalid.html')

# Create your views here.