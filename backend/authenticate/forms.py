from django import forms
from allauth.account.forms import LoginForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit, Div
from django.utils.translation import ugettext as _


class PoeLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(PoeLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.EmailInput()
        self.fields['password'].widget = forms.PasswordInput()

        self.helper = FormHelper()
        self.helper.form_class = 'svg-animation-form'
        self.helper.label_class = 'col-md-2 col-lg-2 col-sm-8'
        self.helper.field_class = 'col-md-8 col-lg-8 col-sm-8'
        self.helper.layout = Layout(
            Field('login', id='email', placeholder='Email Address', type='text', css_class='form-control'),
            Div(css_class='form-group row'),
            Field('password', id='password', type='password', placeholder='Password', css_class='form-control'),
            Div(css_class='form-group row'),
            ButtonHolder(
                Submit('submit', 'Log in', css_class='btn btn-success btn-block')
            )
        )
        super(PoeLoginForm, self).__init__(*args, **kwargs)



class SignupForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(SignupForm, self).__init__( *args, **kwargs)
		self.fields['email'].widget = forms.EmailInput()
		self.fields['username'].widget = forms.CharField(max_length=30)

		self.helper = FormHelper()
		self.helper.form_class = 'svg-animation-form'
		self.helper.label_class = 'col-md-2 col-lg-2 col-sm-8'
		self.helper.field_class = 'col-md-8 col-lg-8 col-sm-8'
		self.helper.layout = Layout(
			Field('email', placeholder='Email', autocomplete='off', css_class='form-control'),
			Div(css_class='form-group row'),
			Field('username', placeholder='Name', autocomplete='off', css_class='form-control'),
			Div(css_class='form-group row'),
    		Field('password1', placeholder='Password', autocomplete='off', css_class='form-control'),
    		Div(css_class='form-group row'),
    		Field('password2', placeholder='Repeat Password', autocomplete='off', css_class='form-control'),
			Div(css_class='form-group row'),
  			ButtonHolder(
  				Submit('submit', 'Signup', css_class='btn btn-theme btn-block')
  				)
  			)
		super(SignupForm, self).__init__(*args, **kwargs)

	def signup(self, request, user):
		user.email = self.cleaned_data['email']
		user.username = self.cleaned_data['username']

		user.save()
