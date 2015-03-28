from django.shortcuts import render, get_object_or_404
from works.models import WorkItem,WorkType

def home(request):

	return render(request, 'main/index.html')

def works(request):
	types = WorkType.objects.all()
	works = WorkItem.objects.all()
	context = {
		'pagetype':'portfolio',
		'works':works,
		'types':types
		}

	return render(request, 'works/works.html',
		context)

def single_work(request, work_pk):
	work = get_object_or_404(WorkItem,pk=work_pk)
	prev = work.get_prev()
	next = work.get_next()
	context = {
		'pagetype':'single single-portfolio',
		'work':work,
		'prev':prev,
		'next':next
		}
	return render(request, 'works/single_work.html',
		context)

def contacts(request):
	context = {'pagetype':'single single-portfolio'}
	return render(request, 'main/contacts.html',
		context)
