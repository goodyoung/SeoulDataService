from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView,  CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

from .models import SeoulData
from django.utils import timezone

# Create your views here.
class MainView(TemplateView) :
    template_name = "web/main.html"
    
    def get_context_data(self, **kwargs: str) -> dict[str, str]:
        context =  super().get_context_data(**kwargs)
        context["name"] = "My project"
        return context

# class CarCreateView(CreateView) :
#     model = SeoulData
#     fields = "__all__"
#     success_url = reverse_lazy("web:car-list")

#     def form_valid(self, form) : 
#         print(form.cleaned_data)
#         return super().form_valid(form)

class OpenListView(ListView) :
    model = SeoulData
    paginate_by = 100

    queryset = SeoulData.objects.all()
    def get_context_data(self, **kwargs) : 
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

class OpenDetailView(DetailView) :
    model = SeoulData

# class CarUpdateView(UpdateView) : 
#     model = Car
#     fields =  ["brand", "model", "color", "year"]
#     success_url = reverse_lazy("web:car-list")

#     template_name_suffix = "_update_form"

# class CarDeleteView(DeleteView) :
#     model = Car
#     success_url = reverse_lazy("web:car-list")
