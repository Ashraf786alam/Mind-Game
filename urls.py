from Quiz import views
from django.conf.urls import url

urlpatterns = [
url('home',views.homepage),
url('Answer',views.Answerpage),
url('signup',views.signuppage),
url('emailcheck',views.Emailcheckpage),
url('Login',views.loginpage),
url('start',views.startpage),
url('logout',views.logoutpage),
]
