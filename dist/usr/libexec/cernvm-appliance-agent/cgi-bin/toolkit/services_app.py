#!/usr/bin/python
import sys
import os
if 'MY_HOME' not in os.environ:
    os.environ['MY_HOME']='/usr/libexec/cernvm-appliance-agent'
sys.path.append(os.environ['MY_HOME'] + '/cgi-bin')
sys.path.append(os.environ['MY_HOME'] + '/cgi-bin/toolkit')
sys.path.append(os.environ['MY_HOME'] + '/cgi-bin/chrome')
sys.path.append(os.environ['MY_HOME'] + '/etc/config')
from services import *
from view import *
from cern_vm import Configuration
import cgi
import cgitb
cgitb.enable()
def main():
    '''
    Services application to manage levels of each service.
    It will support only enable/disable for a service.
    Unfinished.
    '''
    form = cgi.FieldStorage()
    
        
    sm=serviceManagerBuilder()
            
    sm=serviceManagerBuilder()
    content=sm.getView()
    config=Configuration()
    view = View(config.system.actions)
    
    view.setContent('Services Management App', content)
    view.output()

if __name__ == '__main__':
    main()
    
