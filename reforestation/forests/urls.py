from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('' ,views.forest, name='forest'),
    path('add_forest' ,views.add_forest, name='add_forest'),
    path('edit_forest/<int:id>' ,views.forest_edit, name='forest-edit'),
    path('delete_forest/<int:id>' ,views.forest_delete, name='forest-delete'),
     path('search-forest' , csrf_exempt(views.search_forest), name='search_forest'),
     path ('export_csv', views.export_csv, name='export-csv'),
     path ('export_pdf', views.export_pdf, name='export-pdf'),


]