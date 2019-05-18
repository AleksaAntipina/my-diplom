from django.shortcuts import render

# Create your views here.

def people_list(request):
	return render(request, 'diplom/people_list.html', {})
