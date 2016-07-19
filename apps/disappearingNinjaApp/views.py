from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'disappearingNinjaApp/index.html')

def ninjas(request):
	context = {
		"displayAll": True
	}
	return render(request, 'disappearingNinjaApp/ninjas.html', context)

def colors(request, ninjacolor):
	context = {
		"displayAll": False,
		"ninjacolor": ninjacolor
	}
	return render(request, 'disappearingNinjaApp/ninjas.html', context)