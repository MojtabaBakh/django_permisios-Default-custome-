from django.shortcuts import render
from rest_framework import response, serializers
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from .models import Student , book
from .serializers import StudentSerializer , UserSerializer , BookSerializer
from rest_framework.permissions import IsAuthenticated , IsAdminUser , IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .permisions import IsSuperUserOrReadOnly , IsAuther


# Create your views here.




class book_list(ListCreateAPIView):
    queryset=book.objects.all()
    serializer_class = BookSerializer
    permission_classes= ((IsAuthenticated,))

class book_update(RetrieveDestroyAPIView) :

    queryset=book.objects.all()
    serializer_class = BookSerializer
    permission_classes= ((IsAuther,))

@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def student_list(request):
    students=Student.objects.all()
    students_serializer=StudentSerializer(students , many = True)
    return Response(students_serializer.data)


class student_list4(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes= ((IsSuperUserOrReadOnly,))




class student_list2(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes= ((IsAdminUser,))


class student_list3(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes= ((IsAuthenticatedOrReadOnly,))
    

@api_view(["GET"])
def student_details(request , pk):
    student=Student.objects.get(id=pk)
    student_serializer=StudentSerializer(student , many = False)
    return Response(student_serializer.data)


@api_view(["POST"])
def student_save(request):
    student=StudentSerializer(data=request.data)
    if (student.is_valid()) :
        student.save()

    return Response(student.data)


@api_view(["POST"])
def student_update(request , pk):
    instance=Student.objects.get(id=pk)
    student=StudentSerializer( instance=instance , data=request.data)
    if(student.is_valid()):
        student.save()

    return Response(student.data)   



@api_view(["DELETE"])
def student_delete(request , pk):
    instance=Student.objects.get(id=pk)
    instance.delete()

    return Response("student deleted")    



@api_view(["POST"])
def registration_view(request):
    if request.method == "POST" :
        data={}
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid() :
            user = serializer.save()
            data["massage"]="Register is done"
            tokenkey = Token.objects.get(user = user).key
            data['token']= tokenkey
        return Response(data)    








