from django.urls import path

from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.ContactListView.as_view(), name="list"),
    path("yeni/", views.ContactCreateView.as_view(), name="create"),
    path("<int:pk>/", views.ContactDetailView.as_view(), name="detail"),
    path("<int:pk>/duzenle/", views.ContactUpdateView.as_view(), name="update"),
    path("<int:pk>/sil/", views.ContactDeleteView.as_view(), name="delete"),
]
