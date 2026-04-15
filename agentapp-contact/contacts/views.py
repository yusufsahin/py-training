from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ContactForm
from .models import Contact


class ContactListView(ListView):
    model = Contact
    context_object_name = "contacts"
    paginate_by = 10


class ContactDetailView(DetailView):
    model = Contact
    context_object_name = "contact"


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("contacts:list")

    def form_valid(self, form):
        messages.success(self.request, "Kayıt başarıyla oluşturuldu.")
        return super().form_valid(form)


class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("contacts:list")

    def form_valid(self, form):
        messages.success(self.request, "Kayıt güncellendi.")
        return super().form_valid(form)


class ContactDeleteView(DeleteView):
    model = Contact
    success_url = reverse_lazy("contacts:list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Kayıt silindi.")
        return super().delete(request, *args, **kwargs)
