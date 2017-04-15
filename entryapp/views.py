from django.shortcuts import render
from django.http import JsonResponse

from .models import Seats
# Create your views here.
def counter(request):
	count = Seats.objects.all().count()
	if request.GET.get('count', False):
		return JsonResponse({'count' : count})
	return render(request, 'counter.html', {'number' : count})

def app(request):
	if request.method == "POST":
		seat_no = request.POST.get('seat_no', False)
		if seat_no and not Seats.objects.filter(seat_no=seat_no):
			Seats.objects.create(seat_no=seat_no)
			return render(request, 'app.html', {'success' : 'Successfully Added Seat Number '+seat_no+'.'})
		else:
			return render(request, 'app.html', {'error' : 'Seat Number '+seat_no+' is already occupied.'})
	return render(request, 'app.html')