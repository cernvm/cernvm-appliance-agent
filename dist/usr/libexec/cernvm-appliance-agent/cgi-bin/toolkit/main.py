#!/usr/bin/python
import sys
import os
if 'MY_HOME' not in os.environ:
    os.environ['MY_HOME']='/usr/libexec/cernvm-appliance-agent'
sys.path.append(os.environ['MY_HOME']+'/cgi-bin/toolkit')
sys.path.append(os.environ['MY_HOME']+'/etc/config')
sys.path.append(os.environ['MY_HOME']+'/cgi-bin/chrome')
from cern_vm import Configuration
from Adapter import GenericAdapter
from view import View
import cgi
import cgitb
cgitb.enable()

def main():
    '''
    gets the ID from the url as key/value=page/action_id
    and through the adapter displays the result of
    the action with ID=action_id. This functionality composed
    with the GenericAdapter help in the portability and API design
    as importing new functions depends now solely on the xml 
    '''
    config=Configuration()
    fs=cgi.FieldStorage()
    ID=fs["page"].value
    view = View(config.system.actions)
    try:
        action=config.system.actions[ID]
    except KeyError as ke:
        view.setContent('Page not found', 'The requested page was not found. Did you type the url manually?')
        view.output()
        return
    adapter=GenericAdapter(ID, view, action.command_groups)
    adapter.page()
    
if __name__ == '__main__':
    main()
