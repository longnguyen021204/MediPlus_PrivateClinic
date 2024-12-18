from flask import render_template, request, redirect
# from flask_login import

from src import services
from src.models import AccountRoleEnum


def index():
    return render_template(template_name_or_list='idx.html')
def appointment():
    return render_template(template_name_or_list='appointment.html')

def enum_to_string(role):
    return role.name

# def signin():
#     if request.method.__eq__('POST'):
#         next_url = request.form.get('next')
#         username_signin = request.form.get('username_signin')
#         password_signin = request.form.get('password_signin')
#
#         account = services.authenticate(username=username_signin, password=password_signin)
#         login_user(account)
#
#         # role = enum_to_string(account.role).lower()
#         if account.role == AccountRoleEnum.PATIENT:
#             return redirect('/' if next_url is None else next_url)
#
#         elif account.role != AccountRoleEnum.ADMIN:
#             return redirect('/employee/' + enum_to_string(account.role).lower())
#         else:
#             return redirect('/admin')