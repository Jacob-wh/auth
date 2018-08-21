from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.


@csrf_exempt
def user_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        user_permission_group_url = User.objects.filter(username=username).values('groups__permissions__menu__url',
                                                                                  'groups__permissions__menu__name')
        user_permission_url = User.objects.filter(username=username).values('user_permissions__menu__url')
        print(user_permission_url)
        data = []
        for item in user_permission_group_url:
            data.append({item['groups__permissions__menu__name']: item['groups__permissions__menu__url']})
        return JsonResponse({"data": data})
    else:
        return JsonResponse({'error': '密码错误或账户不存在'})


@login_required
def user_logout(request):
    logout(request)
    return JsonResponse({'msg': '退出登录'})


def user_create(request):
    pass


def user_delete(request):
    pass


@login_required
@permission_required('account.detail_log', raise_exception=True)
def detail_log(request):
    return JsonResponse({'msg': '查看日志详情'})


@login_required
@permission_required('account.delete_log', raise_exception=True)
def delete_log(request):
    return JsonResponse({'msg': '删除日志'})


@login_required
@permission_required('account.add_log', raise_exception=True)
def add_log(request):
    return JsonResponse({'msg': '增加日志'})


@login_required
@permission_required('account.update_log', raise_exception=True)
def update_log(request):
    return JsonResponse({'msg': '更新日志'})


@login_required
@permission_required('account.share_log', raise_exception=True)
def share_log(request):
    return JsonResponse({'msg': '分享日志'})


@login_required
@permission_required('account.attendance', raise_exception=True)
def attendance(request):
    return JsonResponse({'msg': '签到'})
