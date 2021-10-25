from django.urls import path,include
from feedback_app import views
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf import settings

urlpatterns = [
	#path('', include('feedback_app.urls')),
    path('/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('', views.people, name='people'),
    path('', views.people, name='people'),
    path('users',views.users, name='user'),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path('index', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('rating.html', views.rating, name='rating'),
    path('performance', views.performance, name='performance'),
    path('profile',views.profile, name='profile'),
    path('questions', views.questions, name='questions'),
    path('aadmin', views.admin,name='aadmin'),
    # path('edit/<int:id>', views.update, name='update'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
	path('edit/update/<int:id>', views.update)

]