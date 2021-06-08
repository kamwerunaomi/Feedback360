from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from .models import Department,Notifications,Category,Questions,Answers,Average,Report
from django.contrib.auth import logout
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordResetForm,UserCreationForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages  
from django.views.generic import View
import io
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import FileResponse
from django.template.loader import get_template
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import get_user_model

def login_view(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		#request.session['id']=user_id
		user = authenticate(request,username=username, password=password)
	
		if user is not None:
			login(request,user)
			return redirect("dashboard")
		else:
			return redirect("loginview")

	return render(request, "login.html")


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":'kamwerunaomi@gmail.com',
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	context = {
	"password_reset_form":password_reset_form
	}
	return render(request, "password/password_reset.html", context)

def index(request):
	return render(request, "index.html")

def performance(request):
	return render(request, "performance.html")

def profile(request):
	return render(request,'profile.html')

def questions(request):
	return render(request, 'questions.html')
def admin(request):
	return render(request, 'admin.html')

def users(request):
	return render(request,'user.html')

def rating(request):
	return render(request, "rating.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('signup')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})