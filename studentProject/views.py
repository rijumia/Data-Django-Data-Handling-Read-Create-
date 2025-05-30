from django.shortcuts import render

def homePage(request):
    return render(request, 'home.html')

def studentListPage(request):
    return render(request, 'studentList.html')

def addStudentPage(request):
    return render(request, 'addStudent.html')