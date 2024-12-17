from django import forms
from .models import Student, Address, Student2, Address2, Photo

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']


class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image']


