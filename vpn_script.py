# -*- coding: utf-8 -*-

import ctypes
import os
import http.cookiejar
import urllib.request
import urllib.parse
import sys
import ssl
import random
import string

##############################################################################


class VpnHandler():
    """
    Allow manipulating TopsecVPN via Web

    """

    def random_string(self, len=15):
        """
        generate a string
        return: a string or empty string

        """

        try:
            return ''.join(random.choice(string.digits) for i in range(len))
        except:
            return ''

    def __init__(self, ip='42.99.16.138'):
        """
        Initiating base parameters

        """

        self.base_url = 'https://%s:8080/cgi/maincgi.cgi' % ip

        #cookie support
        self.cj = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(self.cj))

        # solve PKI issue
        ssl._create_default_https_context = ssl._create_unverified_context

        #display banner
        os.system('cls')
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'.center(79))
        print('%%    Welcome to TopsecVPN Handler.   %%'.center(79))
        print('%%            Version: 1.0a           %%'.center(79))
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'.center(79))

    def login(self, passwd, username='wangwei'):
        """
        Login via Web
        :return: length of cookie

        """

        self.post_default(
            param = {
                'username': username,
                'passwd': passwd,
                'loginSubmitIpt': '',
                'Url': 'Index'})
        return len(self.cj)

    def post_default(self, param=''):
        """
        post parameters to base_url by application enctype
        :return: response

        """

        try:
            return self.opener.open(
                self.base_url,
                urllib.parse.urlencode(param).encode('utf-8'))
        except:
            return None

    def post_multipart(self, param=''):
        """
        post parameters to base_url by multipart enctype
        
        """

        boundary = '---------------------------%s' % self.random_string()
        data = []
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_name"\r\n')
        data.append('test1')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_group"\r\n')
        data.append("基础设施室厂家")
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_account_type"\r\n')
        data.append("local")
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_passwd_type"\r\n')
        data.append("plain")
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_passwd"\r\n')
        data.append('123@@qwe')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_passwd_confirm"\r\n')
        data.append('123@@qwe')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_cert_serialnumber"\r\n')
        data.append('')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="cert_file"; filename=""\r\n')
        data.append('Content-Type: application/octet-stream\r\n')
        data.append('')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_invalid"\r\n')
        data.append('no')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_description"\r\n')
        data.append('sdfsdf')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_inherit_attr"\r\n')
        data.append('yes')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_inherit_role"\r\n')
        data.append('yes')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_vip_user"\r\n')
        data.append('no')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_mail"\r\n')
        data.append('234@r432.com')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_phone"\r\n')
        data.append('17701876253')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_hwid_tex"\r\n')
        data.append('')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_sv_ip"\r\n')
        data.append('')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_iv_ip"\r\n')
        data.append('')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_global_config"\r\n')
        data.append('yes')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_passwd_auth"\r\n')
        data.append('yes')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_fail_login_limit"\r\n')
        data.append('yes')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_maxnum_auth_fail"\r\n')
        data.append('5')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_account_locked_time"\r\n')
        data.append('180')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_maxnum_getback"\r\n')
        data.append('5')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_getback_pass_interval"\r\n')
        data.append('0')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_accept_getback_type"\r\n')
        data.append('mail')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_diff_old_pass"\r\n')
        data.append('yes')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_exclude_account_info"\r\n')
        data.append('yes')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_include_char_lower"\r\n')
        data.append('yes')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_include_char_digit"\r\n')
        data.append('yes')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_include_char_punct"\r\n')
        data.append('yes')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_limit_pass_len"\r\n')
        data.append('yes')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_min_pass_len"\r\n')
        data.append('8')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_max_pass_len"\r\n')
        data.append('32')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_force_change_pass"\r\n')
        data.append('yes')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_first_login"\r\n')
        data.append('yes')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_change_pass_interval"\r\n')
        data.append('102')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_invalid_password"\r\n')
        data.append('yes')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_pass_valid_period"\r\n')
        data.append('120')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_maxnum_login_addr"\r\n')
        data.append('0')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_maxnum_seccode"\r\n')
        data.append('7')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_access_ip_range"\r\n')
        data.append('')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_access_time_range"\r\n')
        data.append('')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_account_start_time"\r\n')
        data.append('')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_account_end_time"\r\n')
        data.append('')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_enable_idle_timeout"\r\n')
        data.append('yes')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_session_idle_timeout"\r\n')
        data.append('1800')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_session_life_timeout"\r\n')
        data.append('86400')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_extend_deal_policy"\r\n')
        data.append('firstlogin')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_operation_compress"\r\n')
        data.append('none')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_operation_dns1"\r\n')
        data.append('')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_operation_dns2"\r\n')
        data.append('')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_operation_wins1"\r\n')
        data.append('')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_operation_wins2"\r\n')
        data.append('')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="sv_pf_work_mode"\r\n')
        data.append('transparent')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="sv_na_work_mode"\r\n')
        data.append('transparent')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_version_control"\r\n')
        data.append('default')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="versionRadio"\r\n')
        data.append('standard')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_act"\r\n')
        data.append('modify-info')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_return_key"\r\n')
        data.append('基础设施室厂家')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_name_hidden"\r\n')
        data.append('test1')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_modify_type"\r\n')
        data.append('user')
        data.append('--%s' % boundary)
        data.append('Content-Disposition: form-data; name="aaaa_user_modify_submit"\r\n')
        data.append(' 确定 ')
        data.append('--%s--\r\n' % boundary)
        http_body = '\r\n'.join(data)
        print(http_body)

        try:
            urllib.request.Request(self.base_url + http_body, headers={})
        except:
            return None

    def get_user_info(self, uname='test1'):
        """
        get a page
        return: html string
        """

        resp = self.post_default(
            param = {
                'Url': 'AAAAUser_right',
                'Act': 'user_modify_all',
                'Name': uname,
                #'Group': urllib.parse.quote('基础设施室厂家')
                })
        if resp:
            return resp.read().decode('gbk')

##############################################################################


def cprint(text, color):
        """
        Print colored text in CMD
        color: 0x02-green, 0x04-red, 0x08-intensity, 0x07-reset

        """

        hld = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.SetConsoleTextAttribute(hld, color|0x08)
        print(text)
        ctypes.windll.kernel32.SetConsoleTextAttribute(hld, 0x07)

def main(self):
    """
    Main function

    """

    handler = VpnHandler() #initiate

    print("<Handler>login") #login
    #password = input("password:")
    #if handler.login(password):
    #if handler.login("hBgdFL6L@"):
    #    cprint('Success', 0x02)
    #else:
    #    cprint('Failed', 0x04)
    #    sys.exit()
    handler.post_multipart()

##############################################################################


if __name__ == '__main__':
    main()