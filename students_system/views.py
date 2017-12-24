from django.shortcuts import render, get_object_or_404
from .models import Facultet, Group, Student


def index(request):
    return render(request, 'base.html', {})


def fc_list(request):
    fc_list = Facultet.objects.all().order_by('name')
    return render(request, 'facultets_list.html', {'fc_list': fc_list})


def facultet(request, name):
    facultet = get_object_or_404(Facultet, name=name)
    group_list = Group.objects.filter(departament__facultet__name=facultet.name).order_by('name')
    return render(request, 'groups_list.html', {'group_list': group_list})


def group(request, name):
    group = get_object_or_404(Group, name=name)
    students_list = Student.objects.filter(group=group).order_by('student_person__surname')
    return render(request, 'students_list.html', {'students_list': students_list})
