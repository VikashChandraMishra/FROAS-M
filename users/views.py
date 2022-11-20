from django.shortcuts import redirect, render
from .models import Teacher
from django.http import JsonResponse


def signin(request):
    if request.method == 'GET':
        response = {'success': True, "message": "sign-in form"}
        return render(request, 'signin.html', response)

    elif request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']


        try:
            teacher = Teacher.objects.get(id=id, password=password)
            if teacher:
                if password == teacher.password:
                    request.session['id'] = id
                    return redirect('users:get_profile', str(id))

        except:
            response = {'success': False, "message": "invalid credentials"}
            return render(request, 'signin.html', response)

    return render(request, 'error.html')


def get_profile(request, id):
    if request.session['id'] and request.method == 'GET':
        teacher = Teacher.objects.get(id=id)
        firstname = teacher.firstname
        lastname = teacher.lastname
        email = teacher.email
        subject1 = teacher.subject1
        subject2 = teacher.subject2
        subject3 = teacher.subject3
        subject4 = teacher.subject4
        department = teacher.department
        college = teacher.college
        personal_info = {"success": True, "message": "Fetched details successfully!", "id": id, "firstname": firstname, "lastname": lastname, "email": email,
                         "subject1": subject1, "subject2": subject2, "subject3": subject3, "subject4": subject4, "department": department, "college": college}
        return render(request, 'profile.html', personal_info)

    else:
        return JsonResponse({"success": False, "message": "Could not fetch details!"})


def edit_profile(request, id):

    if request.method == 'GET':
        return render(request, 'editprofile.html', {'id': id})

    elif request.session['id'] and request.method == 'POST':
        try:
            teacher = Teacher.objects.get(id=request.session['id'])
        except:
            return JsonResponse({"success": False, "message": "Teacher Doesn't Exist!"})

        firstname = teacher.firstname
        lastname = teacher.lastname
        email = teacher.email
        subject1 = teacher.subject1
        subject2 = teacher.subject2
        subject3 = teacher.subject3
        subject4 = teacher.subject4
        department = teacher.department
        college = teacher.college
        password = teacher.password

        if request.POST['firstname']:
            firstname = request.POST['firstname']

        if request.POST['lastname']:
            lastname = request.POST['lastname']

        if request.POST['email']:
            email = request.POST['email']

        if request.POST['subject1']:
            subject1 = request.POST['subject1']

        if request.POST['subject2']:
            subject2 = request.POST['subject2']

        if request.POST['subject3']:
            subject3 = request.POST['subject3']

        if request.POST['subject4']:
            subject4 = request.POST['subject4']

        if request.POST['department']:
            department = request.POST['department']

        if request.POST['college']:
            college = request.POST['college']

        if request.POST['password']:
            password = request.POST['password']

        teacher.firstname = firstname
        teacher.lastname = lastname
        teacher.email = email
        teacher.password = password
        teacher.subject1 = subject1
        teacher.subject2 = subject2
        teacher.subject3 = subject3
        teacher.subject4 = subject4
        teacher.department = department
        teacher.college = college

        teacher.save()

        if request.POST['password']:
            del request.session['id']
            return redirect('/')
        else:
            return redirect('users:get_profile', id)

    else:
        return JsonResponse({"success": False, "message": "Could Not Update Details!"})


def signout(request):

    try:
        del request.session['id']
    except:
        response = {"success": False, "message": "already signed-out"}
        return render(request, 'index.html', response)

    return redirect('/')
