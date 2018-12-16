from django.http import HttpResponseRedirect

from login.data_operation.sso_session_operation import SSOSessionOperation


def login_check(func):
    def inner(request, *args, **kwargs):
        if 'username' in request.session:
            res = func(request, *args, **kwargs)
            return res
        else:
            return HttpResponseRedirect('/back_login')
    return inner


def sso_login_check(func):
    def inner(request, *args, **kwargs):
        if request.META.has_key('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        SSP = SSOSessionOperation()
        username = SSP.check_login_by_ip(ip)
        if username:
            res = func(request, *args, **kwargs)
            return res
        else:
            return HttpResponseRedirect('/back_login')
    return inner