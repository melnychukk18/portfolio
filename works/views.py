from django.shortcuts import render, get_object_or_404
from works.models import WorkItem,WorkType

def home(request):
	last_works = WorkItem.objects.all().order_by('-pub_date')[0:3]
	return render(request, 'main/index.html',{
		'last_works':last_works
		})

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
	releated = WorkItem.objects.all().order_by('?')[:3]	
	context = {
		'pagetype':'single single-portfolio',
		'work':work,
		'prev':prev,
		'next':next,
		'releated':releated
		}
	return render(request, 'works/single_work.html',
		context)

def contacts(request):
	context = {'pagetype':'single single-portfolio'}
	return render(request, 'main/contacts.html',
		context)
