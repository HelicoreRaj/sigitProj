from django.urls import include,path,re_path
from .views import UsernameList,EmailList,EmailCSV

urlpatterns = [
	path('username/',UsernameList.as_view(), name='username'),
	path('email/',EmailList.as_view(), name='email'),
	path('email_csv/',EmailCSV, name='email_csv'),
]

