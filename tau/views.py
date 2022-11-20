from django.shortcuts import render, redirect
from django.urls import NoReverseMatch
from django.core.exceptions import ObjectDoesNotExist 
from django.core.files.storage import FileSystemStorage
from .models import Student, Class
from django.http import JsonResponse
from .methods import train, record_screen, record_attendance

def upload(request, id):
    folder='samples/' 
    
    if request.method == 'GET' and request.session['id']:
        response = {'success': True, 'message': 'samples upload form', 'id': id}
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
            
        response = {'id': id, 'success': False, 'message': 'student does not exist!'}
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
        response = {'success': True, 'message': 'class creation form', 'id': id}
        return render(request, 'create.html', response)
    
    elif request.session['id'] and request.method == 'POST':
        
        teacher = id
        course = request.POST['course']
        semester = request.POST['semester']
        subject = request.POST['subject']
        students = Student.objects.all()
        
        c = Class(teacher=teacher, course=course, semester=semester, subject=subject)
        
        c.save()
        c.students.set(students)
        c.save()
        
        
        record_screen(c.id)
        record_attendance(c.id)
                
        return redirect('users:get_profile', id)