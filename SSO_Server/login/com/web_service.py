import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from spyne import ServiceBase, rpc, Iterable, Application, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication

from login.data_operation.server_operation import ServerOperation
from login.data_operation.sso_session_operation import SSOSessionOperation
from login.data_operation.user_operation import UserOperation


class SSOService(ServiceBase):
    @rpc(Unicode, _returns=Iterable(Unicode))
    def ess_information(ctx, data):
        dic = {"a": 1, "b": 2}
        return HttpResponse(json.dumps(dic))

    @rpc(Unicode, Unicode,  _returns=Unicode)
    def check_login(ctx, token, ip):
        # token = 'MRLVNNUQAG'
        # ip = '127.0.0.1'
        username = ''
        SOP = ServerOperation()
        SSP = SSOSessionOperation()
        print token, ip
        check_result = SOP.check_login_by_token(token)
        if check_result.get('flag'):
            find_result = SSP.check_login_by_ip(ip)
            print find_result
            if find_result:
                username = find_result
        return username

    @rpc(Unicode, Unicode, _returns=Unicode)
    def sso_logout(ctx, token, ip):
        # token = 'MRLVNNUQAG'
        # ip = '127.0.0.1'
        username = ''
        SOP = ServerOperation()
        SSP = SSOSessionOperation()
        print token, ip
        check_result = SOP.check_login_by_token(token)
        if check_result.get('flag'):
            SSP.delete_session(ip)
            find_result = SSP.check_login_by_ip(ip)
            print find_result
            if find_result:
                username = find_result
            else:
                username = ''
        return username

    @rpc(_returns=Iterable(Unicode))
    def get_user_list(ctx):
        result = {}
        UOP = UserOperation()
        user_list = UOP.get_all_user()
        result['user_list'] = user_list
        return HttpResponse(json.dumps(result))


application = Application([SSOService],
    tns='spyne.examples.hello',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

# information_app = csrf_exempt(DjangoApplication(application))
