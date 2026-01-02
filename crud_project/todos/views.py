from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.filters import SearchFilter

def home(request):
    return render(request, "index.html")

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer


class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']

