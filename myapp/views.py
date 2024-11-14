from django.shortcuts import render
from rest_framework.decorators import api_view,APIView,action,permission_classes
from rest_framework.response import Response
from .models import Task,Author,Book
from .serializers import TaskSerializer,Bookserializer,Authorserializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound,ValidationError,APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import BasePermission


class outOfStock(APIException):
    status_code = 400
    default_detail = 'Task do not found at the moment'
    default_message = 'Task do not exist'



# custome  permissions

class CustomePermission(BasePermission):
    def has_permission(self, request, view): #to see has permission this view
        
        return True
    def has_object_permission(self, request, view): #has permission to see a spcific object
        return True


# Create your views here.
@api_view(["GET", "POST", "PUT", "DELETE"])
def hello(request):
    return Response('Message:' "Hello world")


@api_view(['GET', 'POST'])
# @permission_classes(IsAuthenticated)
@permission_classes([
    CustomePermission,
    
    
])
def task_list(request):
    # query search
    print(request.GET.get('value'))
    if request.method == 'GET':
        task =Task.objects.all()
        # convert model to json or xml data and xml or json both link to the db.for that initailize the seializer here and here initaileze to the task
        seializer = TaskSerializer(task,many=True)
        return Response(seializer.data)
    
    if request.method == 'POST':

        # serialize initailize incomming request.data
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
@api_view(["GET", "DELETE", "PUT",])
@permission_classes(IsAuthenticated)

def task_details(request,pk):
    try:
        task = Task.objects.get(pk = pk)
    except Task.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    
    if request.method == 'PUT':
        serializer = TaskSerializer(task,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        task.delete()
        return Response(status=204)
    
    
class TaskList(APIView):
    @permission_classes(IsAuthenticated)

    def get(self,request):
        import time
        time.sleep(6)
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        print(request.data)
        # print(request.body)

        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class TaskDetails(APIView):
    @permission_classes(IsAuthenticated)
    def get(self, request,pk):
        try:
            task = Task.objects.get(pk = pk)
        except Task.DoesNotExist:
            # raise ValidationError()
            raise outOfStock()
        
            # return Response(status=status.HTTP_404_NOT_FOUND)
            # raise NotFound(default= f"Task does not exist and id is {pk}")
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    def put(self, request,pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self, request,pk):
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    @action(detail=False)
    def sent_email(self,request):
        return Response({"Message":"Email sent"})
    @action(detail=True)
    def task_details(self,request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise outOfStock()
            # if "x" in serializer.data['title']:
            #     raise ValidationError(detail="Key 'x' is not valid")
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    



    
    
    
# one to many relationship


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = Authorserializer
    
    
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Bookserializer