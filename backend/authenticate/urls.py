from django.urls import path
from allauth.account import views


app_name = 'authenticate'
urlpatterns = [

    #register to otp to email to login
    #path('', IndexView.as_view(), name="index_page"),
    path('', views.login, name="account_login"),
    path('signup', views.signup, name="account_signup"),
    #path('verify', PhoneVerificationView, name="phone_verification_url"),

    #email confirmation
    path('accounts/email', views.email, name="account_email"),
    path('accounts/confirm-email', views.email_verification_sent, name="account_email_verification_sent"),
    path('accounts/confirm-email/<key>', views.confirm_email, name="account_confirm_email"),

    # Profiles
    #path('accounts/profile/', account_profile, name='account_profile'),

    path('logout', views.logout, {'next_page': 'account/logout.html'}, name='logout'),

    #password reset
    path('password/reset', views.password_reset, name="account_reset_password"),
    path('password/reset/done', views.password_reset_done, name="account_reset_password_done"),
    path('password/reset/key/<key>', views.password_reset_from_key, name="account_reset_password_from_key"),
    path('password/reset/key/done/', views.password_reset_from_key_done, name="account_reset_password_from_key_done"),

]

