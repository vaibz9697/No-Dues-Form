   # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import *

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import reverse, HttpResponseRedirect
from django.db.models import Q


def index(request):
    all_students = stud.objects.all()
    return render(request, 'main/index.html', {'all_students':all_students,})

def login_user(request):
    if(request.method == 'GET'):
        return render(request, 'main/login.html', {})
    if(request.method == 'POST'):
        username = request.POST['webmail']
        password = request.POST['password']
        role = request.POST['role']
        role = str(role)
        user = authenticate(username = username, password = password )
        if user is not None:
            if user.is_active:
                login(request, user)
                if (role == 'student'):
                    return redirect('../student_webpage/')
                if (role == 'faculty'):
                    return redirect('../teacher_webpage/')
                if (role == 'hod'):
                    return redirect('../hod_webpage/')
                if (role == 'caretaker'):
                    return redirect('../caretaker_webpage/')
                if (role == 'warden'):
                    return redirect('../warden_webpage/')
                if (role == 'lab'):
                    return redirect('../lab1_webpage/')
                elif role == "gymkhana":
                    return redirect('../gymkhana_webpage/')
                elif role == "onlineCC":
                    return redirect('../onlineCC_webpage/')
                elif role == "ccentre":
                    return redirect('../cc_webpage/')
                elif role == "thesisManager":
                    return redirect('../submitThesis_webpage/')
                elif role == "library":
                    return redirect('../library_webpage/')
                elif role == "assistantRegistrar":
                    return redirect('../assistantRegistrar_webpage/')
                elif role == "Account":
                    return redirect('../account_webpage/')
                else:
                    return redirect('../login')
        else:
            redirect('/login/')




def logout_user(request):
    if(request.method == 'POST'):
        user = request.user.username
        logout(request)
    return redirect('/main/login/')


def lab1_webpage(request):
    if request.method == 'GET':
        lab_webmail = request.user.username
        lab_obj = get_object_or_404(lab1, webmail=lab_webmail)
        all_students = stud.objects.all();
        sls = Stud_Lab_Status.objects.filter(lab = lab_obj);
        for s in all_students:
            try:
                student = Stud_Lab_Status.objects.get(student = s, lab = lab_obj)
            except:
                foo = Stud_Lab_Status.objects.create(lab = lab_obj, student = s, lab_approval = False);
        sls = Stud_Lab_Status.objects.filter(lab = lab_obj);
        return render(request, 'main/lab1_webpage.html', {'lab' : lab_obj, 'students' : all_students, 'studentLabStatus':sls, })
    elif request.method == 'POST':
        lab_webmail = request.user.username
        lab_obj = get_object_or_404(lab1, webmail=lab_webmail)
        all_students = stud.objects.all()
        # fac = Faculty.objects.get(webmail=webmail)
        stud_lab_status = Stud_Lab_Status.objects.all()
        for s in all_students:
            for sls in stud_lab_status:
                if sls.student.webmail == s.webmail:
                    if request.POST.get(s.webmail, "") == 'on':
                        x = Stud_Lab_Status.objects.get(student=s, lab = lab_obj)
                        x.lab_approval = True
                        x.save()
        # print Stud_Faculty_Status.objects.get(student=stud, faculty=fac).faculty_approval
        return redirect("../lab1_webpage/")

def student_webpage(request):
    stud_webmail = request.user.username
    s1 = get_object_or_404(stud, webmail = stud_webmail)
    all_teachers = Faculty.objects.filter(department = s1.department);
    sfs = Stud_Faculty_Status.objects.filter(student = s1);
    return render(request, 'main/student_webpage.html', {'student' : s1, 'teachers' : all_teachers, 'studentFacultyStatus':sfs, })

def teacher_webpage(request):
    if request.method == 'GET':
        fac_webmail = request.user.username
        teacher = get_object_or_404(Faculty, webmail=fac_webmail)
        all_students = stud.objects.filter(department=teacher.department);
        sfs = Stud_Faculty_Status.objects.filter(faculty = teacher);
        for s in all_students:
            try:
                student = Stud_Faculty_Status.objects.get(student = s, faculty = teacher)
            except:
                foo = Stud_Faculty_Status.objects.create(faculty = teacher, student = s, faculty_approval = False, faculty_remarks = "");
        return render(request, 'main/teacher_webpage.html', {'teacher' : teacher, 'students' : all_students, 'studentFacultyStatus':sfs, })
    elif request.method == 'POST':
        webmail = request.user.username
        teacher = get_object_or_404(Faculty, webmail=webmail)
        all_students = stud.objects.filter(department=teacher.department)
        fac = Faculty.objects.get(webmail=webmail)
        stud_fac_status = Stud_Faculty_Status.objects.filter(faculty=fac)
        for s in all_students:
            for sfs in stud_fac_status:
                if sfs.student.webmail == s.webmail:
                    if request.POST.get(s.webmail, "") == 'on':
                        x = Stud_Faculty_Status.objects.get(student=s, faculty=fac)
                        x.faculty_approval = True
                        x.save()
        # print Stud_Faculty_Status.objects.get(student=stud, faculty=fac).faculty_approval
        return redirect("../teacher_webpage/")


def hod_webpage(request):
    if request.method == 'GET':
        hod_webmail = request.user.username
        hod_object = get_object_or_404(hod, webmail=hod_webmail)
        all_students = stud.objects.filter(department=hod_object.department);
        return render(request, 'main/hod_webpage.html', {'teacher' : hod_object, 'students' : all_students, })
    elif request.method == 'POST':
        webmail = request.user.username
        hod_object = get_object_or_404(hod, webmail=webmail)
        all_students = stud.objects.filter(department=hod_object.department)
        for s in all_students:
            if request.POST.get(s.webmail, "") == 'on':
                s.HOD_approval = True
                s.save();
        # print Stud_Faculty_Status.objects.get(student=stud, faculty=fac).faculty_approval
        return redirect("../hod_webpage/")

def caretaker_webpage(request):
    if request.method == 'GET':
        caretaker_webmail = request.user.username
        caretaker_object = get_object_or_404(caretaker, webmail=caretaker_webmail)
        all_students = stud.objects.filter(hostel=caretaker_object.hostel);
        return render(request, 'main/caretaker_webpage.html', {'teacher' : caretaker_object, 'students' : all_students, })
    elif request.method == 'POST':
        webmail = request.user.username
        caretaker_object = get_object_or_404(caretaker, webmail=webmail)
        all_students = stud.objects.filter(hostel=caretaker_object.hostel)
        for s in all_students:
            if request.POST.get(s.webmail, "") == 'on':
                s.caretaker_approval = True
                s.save();
        # print Stud_Faculty_Status.objects.get(student=stud, faculty=fac).faculty_approval
        return redirect("../caretaker_webpage/")

def warden_webpage(request):
    if request.method == 'GET':
        warden_webmail = request.user.username
        warden_object = get_object_or_404(warden, webmail=warden_webmail)
        all_students = stud.objects.filter(hostel=warden_object.hostel);
        return render(request, 'main/warden_webpage.html', {'teacher' : warden_object, 'students' : all_students, })
    elif request.method == 'POST':
        webmail = request.user.username
        warden_object = get_object_or_404(warden, webmail=webmail)
        all_students = stud.objects.filter(hostel=warden_object.hostel)
        for s in all_students:
            if request.POST.get(s.webmail, "") == 'on':
                s.warden_approval = True
                s.save();
        # print Stud_Faculty_Status.objects.get(student=stud, faculty=fac).faculty_approval
        return redirect("../warden_webpage/")


def cc_webpage(request):
    if request.method == 'GET':
        cc_webmail = request.user.username
        cc_object = get_object_or_404(cc, webmail=cc_webmail)
        all_students = stud.objects.all();
        return render(request, 'main/cc_webpage.html', {'teacher' : cc_object, 'students' : all_students, })
    elif request.method == 'POST':
        cc_webmail = request.user.username
        cc_object = get_object_or_404(cc, webmail=cc_webmail)
        all_students = stud.objects.all()
        for s in all_students:
            if request.POST.get(s.webmail, "") == 'on':
                s.CC_approval = True
                s.save();
        # print Stud_Faculty_Status.objects.get(student=stud, faculty=fac).faculty_approval
        return redirect("../cc_webpage/")


def library_webpage(request):
    if request.method == 'GET':
        library_webmail = request.user.username
        library_object = get_object_or_404(library, webmail=library_webmail)
        all_students = stud.objects.all();
        return render(request, 'main/library_webpage.html', {'teacher' : library_object, 'students' : all_students, })
    elif request.method == 'POST':
        webmail = request.user.username
        library_object = get_object_or_404(library, webmail=webmail)
        all_students = stud.objects.all()
        for s in all_students:
            if request.POST.get(s.webmail, "") == 'on':
                s.library_approval = True
                s.save();
        # print Stud_Faculty_Status.objects.get(student=stud, faculty=fac).faculty_approval
        return redirect("../library_webpage/")


def gymkhana_webpage(request):
    if request.method == 'GET':
        gymkhana_webmail = request.user.username
        gymkhana_object = get_object_or_404(gymkhana, webmail=gymkhana_webmail)
        all_students = stud.objects.all();
        return render(request, 'main/gymkhana_webpage.html', {'teacher' : gymkhana_object, 'students' : all_students, })
    elif request.method == 'POST':
        webmail = request.user.username
        gymkhana_object = get_object_or_404(gymkhana, webmail=webmail)
        all_students = stud.objects.all()
        for s in all_students:
            if request.POST.get(s.webmail, "") == 'on':
                s.gymkhana_approval = True
                s.save();
        # print Stud_Faculty_Status.objects.get(student=stud, faculty=fac).faculty_approval
        return redirect("../gymkhana_webpage/")


def onlineCC_webpage(request):
    if request.method == 'GET':
        onlineCC_webmail = request.user.username
        onlineCC_object = get_object_or_404(onlineCC, webmail=onlineCC_webmail)
        all_students = stud.objects.all();
        return render(request, 'main/onlineCC_webpage.html', {'teacher' : onlineCC_object, 'students' : all_students, })
    elif request.method == 'POST':
        webmail = request.user.username
        onlineCC_object = get_object_or_404(onlineCC, webmail=webmail)
        all_students = stud.objects.filter(hostel=onlineCC_object.hostel)
        for s in all_students:
            if request.POST.get(s.webmail, "") == 'on':
                s.online_cc_approval = True
                s.save();
        # print Stud_Faculty_Status.objects.get(student=stud, faculty=fac).faculty_approval
        return redirect("../onlineCC_webpage/")



def submitThesis_webpage(request):
    if request.method == 'GET':
        submitThesis_webmail = request.user.username
        submitThesis_object = get_object_or_404(submitThesis, webmail=submitThesis_webmail)
        all_students = stud.objects.all();
        return render(request, 'main/submitThesis_webpage.html', {'teacher' : submitThesis_object, 'students' : all_students, })
    elif request.method == 'POST':
        webmail = request.user.username
        submitThesis_object = get_object_or_404(submitThesis, webmail=webmail)
        all_students = stud.objects.filter(hostel=submitThesis_object.hostel)
        for s in all_students:
            if request.POST.get(s.webmail, "") == 'on':
                s.submit_thesis = True
                s.save();
        # print Stud_Faculty_Status.objects.get(student=stud, faculty=fac).faculty_approval
        return redirect("../submitThesis_webpage/")


def account_webpage(request):
    if request.method == 'GET':
        account_webmail = request.user.username
        account_object = get_object_or_404(account, webmail=account_webmail)
        all_students = stud.objects.all();
        return render(request, 'main/account_webpage.html', {'teacher' : account_object, 'students' : all_students, })
    elif request.method == 'POST':
        webmail = request.user.username
        account_object = get_object_or_404(account, webmail=webmail)
        all_students = stud.objects.all()
        for s in all_students:
            if request.POST.get(s.webmail, "") == 'on':
                s.account_approval = True
                s.save();
        # print Stud_Faculty_Status.objects.get(student=stud, faculty=fac).faculty_approval
        return redirect("../account_webpage/")

def assistantRegistrar_webpage(request):
    if request.method == 'GET':
        assistantRegistrar_webmail = request.user.username
        assistantRegistrar_object = get_object_or_404(assistantRegistrar, webmail=assistantRegistrar_webmail)
        all_students = stud.objects.all();
        return render(request, 'main/assistantRegistrar_webpage.html', {'teacher' : assistantRegistrar_object, 'students' : all_students, })
    elif request.method == 'POST':
        webmail = request.user.username
        account_object = get_object_or_404(assistantRegistrar, webmail=webmail)
        all_students = stud.objects.all()
        for s in all_students:
            if request.POST.get(s.webmail, "") == 'on':
                s.assistant_registrar_approval = True
                s.save();
        # print Stud_Faculty_Status.objects.get(student=stud, faculty=fac).faculty_approval
        return redirect("../assistantRegistrar_webpage/")