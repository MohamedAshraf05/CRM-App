from django.shortcuts import render ,redirect
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth import get_user_model
from django.views.generic import ListView , DetailView , DeleteView , UpdateView , CreateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , authenticate , logout
from django.urls import reverse_lazy
from .models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class login_view(LoginView):
    template_name = 'pages/login.html'
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("crm:crm-view")
    
class registrationView(FormView):
    template_name = "pages/registration.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("crm:login")

    def form_valid(self, form) :
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(registrationView , self).form_valid(form)
    
    def get(self,*args,**kwargs ):
        if self.request.user.is_authenticated :
            return redirect('Edu:login')
        return super(registrationView , self ).get(*args,**kwargs)

class CrmView(LoginRequiredMixin,ListView):
    queryset = Customer.objects.all()
    template_name = "pages/home.html"
    context_object_name = 'customers'
    login_url = reverse_lazy('crm:login')
class CrmDetailView(LoginRequiredMixin , DetailView):
    queryset = Customer.objects.all()
    template_name = "pages/detail.html"
    context_object_name = "customersDetails"
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class DeleteCrmView(LoginRequiredMixin , DeleteView):
    queryset = Customer.objects.all()
    template_name = 'pages/delete.html'
    success_url = reverse_lazy('crm:crm-view')


class UpdateCrmView(LoginRequiredMixin , UpdateView):
    model = Customer
    fields = "__all__"
    template_name = 'pages/update.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('crm:crm-view')

class CreateCrmView(LoginRequiredMixin , CreateView):
    model = Customer
    fields = "__all__"
    template_name = 'pages/create.html'
    success_url = reverse_lazy('crm:crm-view')
    context_object_name = 'customer'

def logoutView(request):
    logout(request)
    return redirect('crm:login')

