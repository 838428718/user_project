
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from app.models import User


def index(request):

    return render(request, 'index.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    else:
        json_response = {
            'status': '',
            'data': ''
        }
        account = request.POST.get('account')
        user_password = request.POST.get('user_password')

        users = User.objects.filter(account=account)

        if users.exists():
            user = users.first()
            if user.password == user_password:
                # 登录成功
                request.session['uid'] = user.uid
                json_response['status'] = '200'

                return JsonResponse(json_response)
            else:
                json_response['status'] = '101'
        else:
            json_response['status'] = '101'

        return JsonResponse(json_response)


def logout(request):
    request.session.flush()
    return redirect(reverse('app:login'))

# 用户展示接口
def show_item(request):
    json_response = {
        'status': '200',
        'data': []
    }
    user_id = request.session.get('uid')
    users = User.objects.filter(uid=user_id)
    users_level = users.first().group.level
    show_users = User.objects.filter(Q(group__level__lte=users_level) & Q(is_delete=0))
    paginator = Paginator(show_users, 5)
    page = request.GET.get('page')
    if int(page) <= 0:
        page = 1
    elif int(page) > 5:
        page = 5
    try:
        users_item = paginator.page(page)
    except PageNotAnInteger:
        users_item = paginator.page(1)
        page = 1
    except EmptyPage:
        users_item = paginator.page(paginator.num_pages)
        page = paginator.num_pages
    json_response['page'] = page
    for item in users_item:
        user_data = {
            'uid': item.uid,
            'user_name': item.user_name,
            'age': item.age,
            'group': item.group.group_name,
            'phone': item.phone
        }
        json_response['data'].append(user_data)
    return JsonResponse(json_response)


# 将该用户逻辑删除
def delete_user(request):
    json_response = {
        'status': '200',
        'data': []
    }
    uid = request.GET.get('uid')
    print(uid)
    user = User.objects.get(uid=uid)
    user.is_delete = 1
    user.save()
    return JsonResponse(json_response)

# 编辑用户类
def edit_user(request):
    json_response = {
        'status': '200',
        'data': []
    }

    uid = request.GET.get('uid')
    user_name = request.GET.get('uid')
    phone = request.GET.get('phone')
    age = request.GET.get('age')
    group = request.GET.get('group')
    user = User.objects.get(uid=uid)
    user.user_name = user_name
    user.phone = phone
    user.age = age
    user.group = group

    return JsonResponse(json_response)


# 用户信息展示
def show_user_info(request):
    json_response = {
        'status': '200',
        'data': []
    }
    uid = request.GET.get('uid')
    user = User.objects.get(uid=uid)
    user_data = {
        'userName': user.user_name,
        'group': user.group.group_name,
        'age': user.age,
        'phone': user.phone
    }
    json_response['data'] = user_data
    print(json_response)
    return JsonResponse(json_response)