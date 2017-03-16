from django.shortcuts import render
from django.views.generic import CreateView
from models import Participant
# Create your views here.
class RegisterView(CreateView):
	model = Participant
	fields = ['name', 'gender', 'phone', 'email']
	template_name = 'register.html'
	success_url = "."
	def post(self, request, *args, **kwargs):
		res = super(RegisterView, self).post(request, *args, **kwargs)
		if self.model.objects.filter(email=request.POST.get('email', '')):
			context = self.get_context_data(*args, **kwargs)
			context['registered'] = True
			return render(request, self.template_name, context=context)
		return res