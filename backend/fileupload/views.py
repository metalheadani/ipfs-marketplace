from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from fileupload.models import FileUpload, IpfsAddress
from .forms import FileUploadForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from ipfs.ipfsdml import setter, getter

@login_required
def index(request):
	template_name='fileupload/home.html'
	try:
		users = User.objects.get(id=request.user.id)
	except User.DoesNotExist:
		users = None

	if request.method == 'POST':
		form = FileUploadForm(request.POST, request.FILES)
		if form.is_valid():
			fileform  = form.save(commit=False)
			fileform.user = request.user
			fileform.save()
			selectObject = FileUpload.objects.all().last()
			selectFile = selectObject.file
			sendipfs = setter(selectFile)
			addrsaving = IpfsAddress(file=FileUpload.objects.all().last(),value=sendipfs)
			print(addrsaving.value)
			addrsaving.user = request.user
			addrsaving.save()
			return render(request, 'fileupload/hashsaved.html', {'addrsaving':addrsaving})
		else:
			return HttpResponse('Form NOT valid')

	else:
		form = FileUploadForm()

	context = {'users' : users, 'form' : form}
	return render(request, template_name, context)


@login_required
def UploadedFilesView(request):
	template_name = 'fileupload/uploadedfiles.html'
	print('filessad')
	files = FileUpload.objects.all()
	if files is None:
		return HttpResponse("Upload a file first")
	else:
		context={'files' : files}
		return render(request, template_name, context)


#def fileinfo(request, file_id)


@login_required
def downloadfile(request, file_id):
	template_name = 'fileupload/payment.html'
	#showinfo = get_object_or_404(FileUpload, pk=file_id)
	selectfile = IpfsAddress.objects.get(id=file_id)
	fileaddr = selectfile.value
	getfile = getter(fileaddr)
	context = {}
	return render(request, template_name, context)
