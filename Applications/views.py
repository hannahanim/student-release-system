from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student,Administrator,Application,Mentor

from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q

def index(request):
    return render(request,"index.html")

def program(request):
    return render(request,"program.html")

def login(request):
    return render(request,"login.html")

def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            student = Student.objects.get(student_id=username, passwordstud=password)
            request.session['student_id'] = username
            return HttpResponseRedirect(reverse('student_page') + '?message=success')
        except Student.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            return HttpResponseRedirect(reverse('student_login') + '?message=error')
    return render(request, 'loginstud.html', {'message': ''})

def student_page(request):
    loggedin_studentid = request.session.get('student_id')
    if loggedin_studentid:
        try:
            student = Student.objects.get(student_id=loggedin_studentid)
            applications = Application.objects.filter(student_id=loggedin_studentid).order_by('id') #ascending order
            context = {
                'student': student,
                'applications': applications,  # Pass the applications data to the template
            }
            return render(request, 'student.html', context)
        except Student.DoesNotExist:
            return redirect('loginstud')  # Redirect to the login page or handle this case appropriately
    else:
        return redirect('loginstud')  # Redirect to the login page or handle this case appropriately
    
def form(request):
    displaystud = Application.objects.all().values()
    student = Student.objects.all()

    loggedin_student_id = request.session.get('student_id')
    mystudent = Student.objects.get(student_id=loggedin_student_id) if loggedin_student_id else None

    if request.method == 'POST':
        studid = request.POST.get('student_id')
        datestart = request.POST.get('date_start')
        datefinish = request.POST.get('date_finish')
        totalleave = request.POST.get('total_leave')
        reason = request.POST.get('reason')
        place = request.POST.get('place')
        classestobemissed = request.POST.get('classestobemissed')

        is_valid_input = True  # Placeholder for validation logic
        
        if is_valid_input:
            data = Application(student_id_id=studid, date_start=datestart, date_finish=datefinish, total_leave=totalleave, reason=reason, place=place, classestobemissed=classestobemissed)
            data.save()

            return HttpResponseRedirect(reverse('form') + '?success=true')
        else:
            return HttpResponseRedirect(reverse('form') + '?success=false')

    context = {
        'displaystud': displaystud,
        'student': student,
        'mystudent':mystudent
    }
    return render(request, "form.html", context)

def search_status2(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        loggedin_studentid = request.session.get('student_id')
        
        if loggedin_studentid:
            try:
                student = Student.objects.get(student_id=loggedin_studentid)
                applications = Application.objects.filter(student_id=loggedin_studentid, status=status) if status else Application.objects.filter(student_id=loggedin_studentid)
            except Student.DoesNotExist:
                return redirect('loginstud') 
        else:
            return redirect('loginstud')  

        context = {'student': student, 'applications': applications}
        return render(request, 'student.html', context)
    else:
        return render(request, 'student.html')

def studdprofile(request, student_id):
    student = Student.objects.get(student_id=student_id)
    mentor = student.mentor_id
    context = {
        'student': student,
        'mentor': mentor  
    }
    return render(request, "studentdata.html", context)

def updatestuddata(request, student_id):
    passwordstud=request.POST['passwordstud']
    data=Student.objects.get(student_id=student_id)
    data.passwordstud=passwordstud
    data.save()

    return HttpResponseRedirect(reverse("studdprofile", args=[student_id]) + '?success=true')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            admin = Administrator.objects.get(admin_id=username, passwordadmin=password)
            request.session['admin_id'] = username
            return HttpResponseRedirect(reverse('admin_page') + '?login_message=success')
        except Administrator.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            return HttpResponseRedirect(reverse('admin_login') + '?message=error')
        
    return render(request, 'loginadmin.html', {'message': ''})

def admin_page(request):
    loggedin_adminid = request.session.get('admin_id')
    admin = Administrator.objects.get(admin_id=loggedin_adminid)
    applications = Application.objects.all().order_by('id') #ascending order
    context = {
        'admin': admin,
        'applications': applications,  # Pass the applications data to the template
    }
    return render(request, 'admin.html', context)

def update(request,id):
    updatestatus=Application.objects.get(id=id)
    dict={
        'updatestatus':updatestatus
    }
    return render(request,"update.html",dict)

def updatestatus(request,id):
    status=request.POST['status']
    data=Application.objects.get(id=id)
    data.status=status
    data.save()

    return HttpResponseRedirect(reverse("update", args=[id]) + '?success=true')
    
def viewdelete(request,id):
    datanakdelete=Application.objects.get(id=id)
    dict={
        'datatobedelete':datanakdelete
    }
    return render(request,"delete.html",dict)

def delete(request, id):
    deleteapplicant = Application.objects.get(id=id)
    deleteapplicant.delete()
    return HttpResponseRedirect(reverse("admin_page") + "?delete_message=success")

def search_status(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        applications = Application.objects.filter(status=status) if status else Application.objects.all()
        loggedin_adminid = request.session.get('admin_id')
        try:
            admin = Administrator.objects.get(admin_id=loggedin_adminid)
        except Administrator.DoesNotExist:
            return redirect('loginadmin')  # Redirect to the login page or handle this case appropriately

        context = {'admin': admin, 'applications': applications}
        return render(request, 'admin.html', context)
    else:
        return render(request, 'admin.html')

def adminprofile(request, admin_id):
    admin=Administrator.objects.get(admin_id=admin_id)
    context={
        'admin':admin
    }
    return render(request,"admindata.html",context)

def updateadmin(request, admin_id):
    admin_number=request.POST['admin_number']
    passwordadmin=request.POST['passwordadmin']
    data=Administrator.objects.get(admin_id=admin_id)
    data.admin_number=admin_number
    data.passwordadmin=passwordadmin
    data.save()

    return HttpResponseRedirect(reverse("adminprofile", args=[admin_id]) + '?success=true')

def mentor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            mentor = Mentor.objects.get(mentor_id=username, passwordmentor=password)
            request.session['mentor_id'] = username
            return HttpResponseRedirect(reverse('mentor_page') + '?message=success')
        except Mentor.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            return HttpResponseRedirect(reverse('mentor_login') + '?message=error')

    return render(request, 'loginmentor.html', {'message': ''})

def mentor_page(request):
    loggedin_mentorid = request.session.get('mentor_id')
    mentor = Mentor.objects.get(mentor_id=loggedin_mentorid)
    applications = Application.objects.filter(student_id__mentor_id=mentor).order_by('id')
    context = {
        'mentor': mentor,
        'applications': applications,  
    }
    return render(request, 'mentor.html', context)
        
def searchpage(request):
    search_query = request.GET.get('search', '')
    loggedin_mentorid = request.session.get('mentor_id')
    if loggedin_mentorid:
        try:
            mentor = Mentor.objects.get(mentor_id=loggedin_mentorid)
            if search_query:
                applications = Application.objects.filter(Q(student_id__student_id__icontains=search_query) & Q(student_id__mentor_id=mentor))
            else:
                applications = Application.objects.filter(student_id__mentor_id=mentor)
            context = {
                'mentor': mentor, 
                'applications': applications
            }
            return render(request, 'mentor.html', context)
        except Mentor.DoesNotExist:
            return redirect('loginmentor')  # Redirect to the mentor login page or handle this case appropriately
    else:
        return redirect('loginmentor')  # Redirect to the mentor login page or handle this case appropriately
    
def student_profile(request, student_id):
    student = Student.objects.get(student_id=student_id)
    mentor = student.mentor_id
    context = {
        'student': student,
        'mentor': mentor  
    }
    return render(request, "studentprofile.html", context)

def studupdate(request, student_id):
    student = Student.objects.get(student_id=student_id)
    mentor = student.mentor_id
    context = {
        'student': student,
        'mentor': mentor  
    }
    return render(request, "updatestud.html", context)

def viewupdate(request, student_id):
    class_stud = request.POST.get('class_stud', '')
    student_number = request.POST.get('student_number', '')
    parent_name = request.POST.get('parent_name', '')
    parent_number = request.POST.get('parent_number', '')
    parent_adress = request.POST.get('parent_adress', '')

    data = Student.objects.get(student_id=student_id)
    data.class_stud = class_stud
    data.student_number = student_number
    data.parent_name = parent_name
    data.parent_number = parent_number
    data.parent_adress = parent_adress

    data.save()

    return HttpResponseRedirect(reverse("student_profile", args=[student_id]) + '?success=true')

def viewdelete2(request,id):
    datanakdelete=Application.objects.get(id=id)
    dict={
        'datatobedelete':datanakdelete,
    }
    return render(request,"delete2.html",dict)

def delete2(request, id):
    deleteapplicant = Application.objects.get(id=id)
    deleteapplicant.delete()
    return HttpResponseRedirect(reverse("mentor_page") + "?delete_message=success")

def mentorprofile(request, mentor_id):
    mentor=Mentor.objects.get(mentor_id=mentor_id)
    context={
        'mentor':mentor
    }
    return render(request,"mentordata.html",context)

def updatementor(request,mentor_id):
    mentor_number=request.POST['mentor_number']
    email=request.POST['email']
    passwordmentor=request.POST['passwordmentor']
    data=Mentor.objects.get(mentor_id=mentor_id)
    data.mentor_number=mentor_number
    data.email=email
    data.passwordmentor=passwordmentor
    data.save()

    return HttpResponseRedirect(reverse("mentorprofile", args=[mentor_id]) + '?success=true')
