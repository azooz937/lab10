from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Address, Photo
from .forms import StudentForm, AddressForm, StudentForm, Student2Form, PhotoForm

def list_students(request):
    students = Student.objects.all()
    return render(request, 'student/list_students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'student/add_student.html', {'form': form})

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/update_student.html', {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('list_students')
    return render(request, 'student/delete_student.html', {'student': student})


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_photos')
    else:
        form = PhotoForm()
    return render(request, 'photos/upload_photo.html', {'form': form})

def list_photos(request):
    photos = Photo.objects.all()
    return render(request, 'photos/list_photos.html', {'photos': photos})
