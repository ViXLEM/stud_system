from django.contrib import admin

from .models import Student, Adress, Facultet, Departament, Speciality, Group, Person

admin.site.register(Student)
admin.site.register(Adress)
admin.site.register(Facultet)
admin.site.register(Departament)
admin.site.register(Speciality)
admin.site.register(Group)
admin.site.register(Person)
