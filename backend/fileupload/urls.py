from django.urls import path
from . import views

app_name='fileupload'

urlpatterns = [
	path('', views.index, name='index'),
	path('uploads', views.UploadedFilesView, name='uploaded_files_view'),
	path('uploads/<int:file_id>', views.downloadfile, name='downloadfile'),
	        
]

