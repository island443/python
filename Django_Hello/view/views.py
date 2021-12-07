from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from db.models import models, TblEmp, TblDept
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers

# Paginator用来实现分页   EmptyPage用来判断页面是否存在  PageNotAnlnteger用来判断输入的页面是否为整数
import json


def index(request):
    emps = TblEmp.objects.all()
    lists = Paginator(emps, 5)  # 一个页面显示5条数据

    pages = request.GET.get('pn')  # 接收一个GET请求传来的页码数

    data = lists.page(pages)

    couts = lists.count  # 总数据条数
    num_pages = lists.num_pages  # 总页数

    json_data = serializers.serialize("json", data.object_list)

    return JsonResponse(json_data, safe=False)



def emp_delete(request):
    pk = request.GET.get("empId")  # 获取前端传来的id值
    TblEmp.objects.filter(emp_id=pk).delete()
    return redirect('http://localhost:8000/view/emps?pn=1')  # 进行重定向


def emp_deletes(request):
    pks = request.GET.get("del_idstr")
    lst = pks.split('-')

    for i in lst:
        TblEmp.objects.filter(emp_id=i).delete()

    return redirect('http://localhost:8000/view/emps?pn=1')


def depts(request):
    dept = TblDept.objects.all()
    json_dept_data = serializers.serialize("json", dept)

    return JsonResponse(json_dept_data, safe=False)


def addemp(request):
    empName = request.GET.get("empName")

    email = request.GET.get("email")

    gender = request.GET.get("gender")

    dId = request.GET.get("dId")

    obj = TblEmp.objects.create(emp_name=empName, email=email, gender=gender, d=TblDept.objects.get(pk=dId))

    json_data = [{"status": "success"}]

    return JsonResponse(json_data, safe=False)


def query_emp(request):
    pk = request.GET.get("id")

    empobj = TblEmp.objects.filter(pk=pk)

    json_data = serializers.serialize("json", empobj)

    return JsonResponse(json_data, safe=False)


def modify_emp(request):
    pk = request.GET.get("id")
    print(pk)
    email = request.GET.get("email")
    print(email)
    gender = request.GET.get("gender")
    print(gender)
    dId = request.GET.get("dId")
    print(dId)

    empobj = TblEmp.objects.get(pk=pk)
    empobj.gender = gender
    empobj.email = email
    empobj.dId = dId
    empobj.save()

    json_data = [{"status": "success"}]

    return JsonResponse(json_data, safe=False)


def pages(request):
    currentpage = request.GET.get("currentPage")

    emps = TblEmp.objects.all()
    lists = Paginator(emps, 5)  # 一个页面显示5条数据
    data = lists.page(currentpage)

    has_next=data.has_next()            # 有下一页
    has_previous=data.has_previous()    # 有上一页
    data_number=data.number         # 当前页码

    page_range=lists.page_range
    lst=[]
    for i in page_range:
        lst.append(i)

    couts = lists.count  # 总数据条数
    num_pages = lists.num_pages  # 总页数





    context = {"couts": couts, "num_pages": num_pages,"has_next":has_next,"has_previous":has_previous,"data_number":data_number,"page_range":lst}

    return JsonResponse(context, safe=False)









def home(request):
    msgList = TblEmp.objects.filter(emp_id__isnull=False)
    context = {"msglist": msgList}
    return render(request, 'Index/home.html', context)
