from django.db import models


class Adress(models.Model):
    city = models.CharField(max_length=32, default='Київ')
    street = models.CharField(max_length=32, default='Незалежності')
    build = models.CharField(max_length=32, default='1')
    flat = models.IntegerField()

    def __str__(self):
        return 'м. {}, вул. {}, {}, {}'.format(self.city, self.street,
                                               self.build, self.flat)


class Person(models.Model):
    passport = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    birthday_date = models.DateField()
    sex = models.CharField(max_length=5, choices=(('male', 'male'),
                                                  ('female', 'female')))
    adress = models.ForeignKey(Adress)

    def __str__(self):
        return '{} {} ({})'.format(self.surname, self.name, self.passport)


class Facultet(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    main_person = models.ForeignKey(Person)
    adress = models.ForeignKey(Adress)

    def __str__(self):
        return '{}'.format(self.name)


class Departament(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    facultet = models.ForeignKey(Facultet)
    main_person = models.ForeignKey(Person)
    adress = models.ForeignKey(Adress)

    def __str__(self):
        return '{}'.format(self.name)


class Speciality(models.Model):
    code = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return '{} ({})'.format(self.name, self.code)


class Group(models.Model):
    name = models.CharField(max_length=5, primary_key=True)
    departament = models.ForeignKey(Departament)
    speciality = models.ForeignKey(Speciality)
    form_of_education = models.CharField(max_length=16, choices=(('full_time', 'денна'),
                                                  ('external', 'заочна')))

    def __str__(self):
        return '{}'.format(self.name)


class Student(models.Model):
    gradebook = models.CharField(max_length=16, primary_key=True)
    student_person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    student_card = models.CharField(max_length=10)
    atestat = models.CharField(max_length=16)

    def __str__(self):
        return '{}'.format(self.student_person)
