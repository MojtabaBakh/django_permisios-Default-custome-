
from django.contrib import admin
from django.urls import path

from .views import student_list,book_update , book_list ,student_list4 ,student_list2 ,student_list3 ,student_details , student_save , student_update , student_delete , registration_view

urlpatterns = [
    path('student_list/', student_list),
    path('student_list4/', student_list4.as_view()     ),
    path('student_list2/',   student_list2.as_view()   ),
    path('student_list3/',   student_list3.as_view()   ),
    path('book_list/',   book_list.as_view()   ),
    path('book_update/<pk>', book_update.as_view()),
    path('student_details/<pk>', student_details),
    path('student_save', student_save),
    path('student_update/<pk>', student_update),
    path('student_delete/<pk>', student_delete),
    path('registration_view', registration_view ),
]
