from django import forms
from App.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id',"name","age","gender","phone","email","course","join_date","address","about"]