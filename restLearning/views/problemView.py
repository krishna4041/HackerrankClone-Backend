from rest_framework.views import APIView
from rest_framework import generics,viewsets
from os import remove
from django.http import QueryDict
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from restLearning.models import Problem
from  subprocess import  Popen,PIPE,STDOUT,run
from  threading import Thread
import time
from  restLearning.serializers.problem import *
import json

class ProblemView(APIView):
    # parser_classes = (MultiPartParser,FormParser)

    def post(self,request, *args, **kwargs):
        problem_serialxer = ProblemSerializers(data=request.data)
        # import ipdb
        # ipdb.set_trace()
        if problem_serialxer.is_valid():
            problem_serialxer.save()
            return Response(problem_serialxer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(problem_serialxer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        problems = Problem.objects.all()
        problems = ProblemSerializers(problems,many=True)
        return Response(problems.data,status=status.HTTP_200_OK)

class Problem_by_ID(generics.ListAPIView):
    serializer_class = ProblemSerializers
    model = Problem
    def get_queryset(self):
        id = self.kwargs['id']
        file = open("this_file.c","a")
        file.close()
        remove("this_file.c")
        queryset = self.model.objects.filter(id=id)
        return queryset

@api_view(['GET', 'POST'])
def CompileProblem(request, pk):
    if request.method == 'POST' :
        # import ipdb
        # ipdb.set_trace()
        data = TextBox(data=request.data)
        if data.is_valid():
            file = Problem.objects.get(id=pk)
            file = file.problem_main_file
            file = file.open(mode="r").readlines()
            file.append(data['text_box'].value)
            file = "".join(file)
            result = compile_return_status("test_file.c",file, delete_two_files=True)
            return  Response(result, status=status.HTTP_201_CREATED)

def execute_problem(result):
    proc = Popen(args=["./a.exe"], shell=False, bufsize=1, stdout=PIPE, stderr=STDOUT)
    while (True):
        # Read line from stdout, break if EOF reached, append line to output
        line = proc.stdout.readline()
        line = line.decode()
        if (line == ""): break
        result.append(line)
    print(result)
    remove('a.exe')


@api_view(['GET', 'POST'])
def Runproblem(request, pk):
    if request.method == 'POST':
        data = TextBox(data=request.data)
        if data.is_valid():
            file = Problem.objects.get(id=pk)
            file = file.problem_testcase_file
            file = file.open(mode="r").readlines()
            file.append(data['text_box'].value)
            file = "".join(file)
            result = compile_return_status("test_file.c", file, delete_two_files=False)
            if result == []:
                k = Thread(target=execute_problem,args=(result,))
                k.start()
                time.sleep(7)
                if k.is_alive():
                    promt = run(["taskKill", "/F", "/IM", "a.exe"])
                    result = ["time_limit_exceeded"]
            return Response(result, status=status.HTTP_201_CREATED)


def compile_return_status(file_name,data,delete_two_files):
    file = open(file_name,"a")
    file.write(data)
    file.close()
    output = []
    proc = Popen(args=["gcc", file_name], shell=False, bufsize=1, stdout=PIPE,stderr=STDOUT)
    while (True):
        line = proc.stdout.readline()
        line = line.decode()
        if (line == ""): break
        output.append(line)
    if delete_two_files and output == []:
        remove(file_name)
        remove('a.exe')
    else:
        remove(file_name)
    return output