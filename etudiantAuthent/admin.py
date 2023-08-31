from django.contrib import admin

#from django.contrib import admin

# Register your models here.
from .models import User, Question, Answer, Student, Teacher, Lesson, Comment, Etudiant, Professeur, Modul, Adminis

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(Etudiant)
admin.site.register(Professeur)
admin.site.register(Modul)
admin.site.register(Adminis)

# ************************


