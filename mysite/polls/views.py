# Create your views here.
from django.http import HttpResponse
##from django.template import Context, loader
##from django.http import Http404
from django.shortcuts import render, get_object_or_404

from polls.models import Poll

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {'latest_poll_list': latest_poll_list,}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
##    try:
##        poll = Poll.objects.get(pk=poll_id)
##    except Poll.DoesNotExist:
##        raise Http404
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html',{'poll': poll})

def results(request, poll_id):
    return HttpResponse("Results of poll %s" % poll_id)

def vote(request, poll_id):
    return HttpResponse("Voting on poll %s" % poll_id)
