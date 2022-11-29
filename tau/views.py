from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Student, Class
from django.http import JsonResponse
from .methods import train, record_screen, record_attendance
import datetime

def upload(request, id):
    folder = 'samples/'

    if request.method == 'GET' and request.session['id']:
        response = {'success': True,
                    'message': 'samples upload form', 'id': id}
        return render(request, 'upload.html', response)

    elif request.method == 'POST' and request.FILES.getlist('files') and request.session['id']:
        student_id = request.POST['student_id']

        student = Student.objects.filter(id=student_id)

        if student:
            folder = folder + student_id
            files = request.FILES.getlist('files')
            fs = FileSystemStorage(location=folder)
            for file in files:
                fs.save(file.name, file)

            train()
            return redirect('users:get_profile', str(id))

        response = {'id': id, 'success': False,
                    'message': 'student does not exist!'}
        return render(request, 'upload.html', response)

    else:
        response = {'success': False, 'message': 'sample upload failed'}
        return render(request, 'upload.html', response)


def list(request, id):
    if request.session['id'] and request.method == 'GET':
        return render(request, 'list.html', {'id': id})

    return redirect('/')


def list_data(request, id):
    if request.session['id'] and request.method == 'GET':
        students = Student.objects.values(
            'roll',
            'firstname',
            'lastname',
            'email',
            'course',
            'semester',
            'department',
            'college',
            'id'
        )

        data = []

        for student in students:
            data.append(student)

        return JsonResponse(data, safe=False)

    return redirect('/')


def create_class(request, id):

    if request.session['id'] and request.method == 'GET':
        response = {'success': True,
                    'message': 'class creation form', 'id': id}
        return render(request, 'create.html', response)

    elif request.session['id'] and request.method == 'POST':

        teacher = id
        course = request.POST['course']
        semester = request.POST['semester']
        subject = request.POST['subject']
        students = Student.objects.all()

        c = Class(teacher=teacher, course=course,
                  semester=semester, subject=subject)

        c.save()
        c.students.set(students)
        c.save()

        record_screen(c.id)
        record_attendance(c.id)

        return redirect('users:get_profile', id)


def class_history(request, id):
    if request.session['id'] and request.method == 'GET':
        return render(request, 'class_history.html', {"id": id})

    return redirect('/')


def list_classes(request, id):
    if request.session['id'] and request.method == 'GET':
        classes = Class.objects.values(
            'id',
            'course',
            'semester',
            'subject',
            'date'
        )

        data = []

        for c in classes:
            data.append(c)

        return JsonResponse(data, safe=False)

    return redirect('/')


# def class_details(request, id):
#     if request.session['id'] and request.method == 'GET':
#         c = Class.objects.get(id=id).values(
#             'course',
#             'semester',
#             'subject'
#         )
#         response = {'id': id, 'course': c.course, 'semester': c.semester, 'subject': c.subject}
#         return render(request, 'class_details.html', response)

#     return redirect('/')

# def fetch_class_details(request, id):
#     if request.session['id'] and request.method == 'GET':
#         c = Class.objects.filter(id=id).values(
#             'course',
#             'semester',
#             'subject'
#         )

#         classes = Student.objects.filter(course=c.course, semester=c.semester).values(
#             'id',
#             'course',
#             'semester',
#             'subject'
#         )

#         data = []

#         for c in classes:
#             data.append(c)

#         return JsonResponse(data, safe=False)

#     return redirect('/')


def display(request, id):
    if request.session['id'] and request.method == 'POST':

        subject = request.POST['subject']
        course = request.POST['course']
        semester = request.POST['semester']
        start_date = request.POST['start_date']
        
        class_details = {"subject": subject, "course": course, "semester": semester, "start_date": start_date }
        
        start_yy = int(start_date.split('-')[0])
        start_mm = int(start_date.split('-')[1])
        start_dd = int(start_date.split('-')[2])

        classes = Class.objects.filter(semester=semester, course=course, subject=subject, date__gte=datetime.date(start_yy,start_mm,start_dd)).values('attendance')
        students = Student.objects.filter(course=course, semester=semester).values('id', 'roll', 'firstname', 'lastname')

        attendance = []
        
        for s in students:
            a = {"id": s['id'], "roll": s['roll'], "firstname": s['firstname'], "lastname": s['lastname'], "classes_attended": 0}
            attendance.append(a)
            for c in classes:
                if str(s['id']) in c['attendance'].split(','): 
                    attendance[attendance.index(a)]['classes_attended'] += 1
                
        return render(request, 'display.html', {"id": id, "class_details": class_details, "attendance": attendance})

    return redirect('/')