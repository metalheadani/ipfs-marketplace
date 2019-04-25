from django.forms import ModelForm
from .models import FileUpload
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit, Div
from django.utils.translation import ugettext_lazy as _

class FileUploadForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FileUploadForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Field('name', style='max-width: 15em'),
			Div(css_class='tab-content form-group'),
			Field('price',placeholder='ETH' ,style='max-width: 15em'),
			Div(css_class='tab-content form-group'),
			Field('ethaddress',placeholder='Your receiving ETH address' ,style='max-width: 15em'),
			Div(css_class='tab-content form-group'),
			Field('file'),
			Div(css_class='tab-content form-group'),
			ButtonHolder(
				Submit('submit', 'Save', css_class='btn btn-theme small')
				)
			)
		super(FileUploadForm, self).__init__(*args, **kwargs)

	class Meta:
	    model = FileUpload
	    fields = ['name', 'file','price','ethaddress']
	    labels = {
	    'name' : ('Enter file name'),
	    }


