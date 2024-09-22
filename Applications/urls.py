from django.urls import path
from . import views

urlpatterns = [
    # student urls
    path("", views.index, name="index"),
    path("program/", views.program, name="program"),
    path("login/", views.login, name="login"),
    path("student_login/", views.student_login, name="student_login"),
    path('student', views.student_page, name='student_page'),
    path('form/', views.form, name='form'),
    path('search_status2/', views.search_status2, name='search_status2'),
    path('studentprofile2/<str:student_id>', views.studdprofile, name='studdprofile'),
    path('studentprofile2/updatestuddata/<str:student_id>',views.updatestuddata, name='updatestuddata'),

    # admin urls
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin/', views.admin_page, name='admin_page'),
    path('update/<str:id>', views.update, name='update'),
    path('update/updatedata/<str:id>',views.updatestatus, name='updatestatus'),
    path("viewdelete/<str:id>",views.viewdelete, name="viewdelete"),
    path("viewdelete/delete/<str:id>",views.delete, name="delete"),
    path('search_status/', views.search_status, name='search_status'),
    path('adminprofile/<str:admin_id>', views.adminprofile, name='adminprofile'),
    path('adminprofile/updateadmin/<str:admin_id>',views.updateadmin, name='updateadmin'),

    # mentor urls
    path('mentor_login/', views.mentor_login, name='mentor_login'),
    path('mentor/', views.mentor_page, name='mentor_page'),
    path('searchpage/',views.searchpage,name='searchpage'),
    path("viewdelete2/<str:id>",views.viewdelete2, name="viewdelete2"),
    path("viewdelete2/delete2/<str:id>",views.delete2, name="delete2"),
    path('studentprofile/<str:student_id>', views.student_profile, name='student_profile'),
    path('studentprofile/updatedata/<str:student_id>', views.viewupdate, name='viewupdate'),
    path('studupdate/<str:student_id>', views.studupdate, name='studupdate'),
    path('studupdate/updatedata/<str:student_id>', views.viewupdate, name='viewupdate'),
    path('mentorprofile/<str:mentor_id>', views.mentorprofile, name='mentorprofile'),
    path('mentorprofile/updatementor/<str:mentor_id>',views.updatementor, name='updatementor'),

]