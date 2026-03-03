from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("merge/", views.merge_pdfs, name="merge"),
    path("download/", views.download_pdf, name="download"),
]