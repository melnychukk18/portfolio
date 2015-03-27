from django.shortcuts import render

def home(request):

	return render(request, 'main/index.html')

def works(request):
	context = {'pagetype':'portfolio'}
	return render(request, 'works/works.html',
		context)

def single_work(request):
	context = {'pagetype':'single single-portfolio'}
	return render(request, 'works/single_work.html',
		context)

def contacts(request):
	context = {'pagetype':'single single-portfolio'}
	return render(request, 'main/contacts.html',
		context)
