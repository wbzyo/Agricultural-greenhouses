
from random import randint
from django.core.mail import send_mail
from django.core import mail


def get_random_code(code_length=8):
    code_source = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(code_length):
        code += code_source[randint(0, len(code_source) - 1)]
    return code


def send_email_verify(email):
    code = get_random_code(6)
    send_title = '找回密码'
    send_body = '您的密码是：' + code
    send_mail(send_title, send_body, 'xxxxxxx@qq.com ', [email])
    return code