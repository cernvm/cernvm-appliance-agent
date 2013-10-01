#!/usr/bin/python
import cgi
import cgitb
import os
cgitb.enable()
import sys
sys.path.append(os.environ['MY_HOME']+'/scripts')
sys.path.append(os.environ['MY_HOME']+'/etc/config')
sys.path.append(os.environ['MY_HOME']+'/cgi-bin/chrome')
from PasswordManager import *
from cern_vm import Configuration
from view import View
def main():
    form = cgi.FieldStorage()
    config=Configuration()
    view = View(config.system.actions)
    if "passwd" not in form and "passwd_new1" not in form and "passwd_new2" not in form:
        view.setContent('User management', getView())
        view.output()
    else:
        pm = PasswordManager(form, 'admin')
        try:
            pm.doTransaction()
            view.setContent("User management", getSuccessView())
            view.output()
        except Exception as e:
            view.setContent("User management", getFailedView(e.strerror))
            view.output()
            
if __name__ == '__main__':
    main()
