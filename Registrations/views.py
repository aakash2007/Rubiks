from django.shortcuts import render
from django.views.generic import CreateView
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from models import Participant
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(CreateView):
	model = Participant
	fields = ['name', 'idno', 'phone', 'can_solve', 'institute']
	template_name = 'index.html'
	success_url = '.'
	def get_context_data(self, *args, **kwargs):
		context = super(RegisterView, self).get_context_data(*args, **kwargs)
		context["number"] = Participant.objects.all().count()
		return context
	def get(self, request, *args, **kwargs):
		if request.is_ajax():
			return JsonResponse({'count' : Participant.objects.all().count()})
		return super(RegisterView, self).get(request, *args, **kwargs)
	def post(self, request, *args, **kwargs):
		try:
			Participant.objects.get(idno=request.POST['idno'])
			return JsonResponse({'error' : 1})
		except:
			res = super(RegisterView, self).post(request, *args, **kwargs)
			return JsonResponse({'success' : 1, 'count' : Participant.objects.all().count()})