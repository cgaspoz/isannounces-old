# Create your views here.
from cfp.models import Conference, Call, Deadline
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    latest_editions_deadlines_list = Deadline.objects.filter(call__content_type=12).filter(mandatory=1).order_by('-date')
    latest_journals_deadlines_list = Deadline.objects.filter(call__content_type=13).filter(mandatory=1).order_by('-date')
    latest_books_deadlines_list = Deadline.objects.filter(call__content_type=15).filter(mandatory=1).order_by('-date')
    latest_divisions_deadlines_list = Deadline.objects.filter(call__content_type=17).filter(mandatory=1).order_by('-date')
    return render_to_response('cfp/index.html', {
        'latest_editions_deadlines_list': latest_editions_deadlines_list,
        'latest_journals_deadlines_list': latest_journals_deadlines_list,
        'latest_books_deadlines_list': latest_books_deadlines_list,
        'latest_divisions_deadlines_list': latest_divisions_deadlines_list,
        })