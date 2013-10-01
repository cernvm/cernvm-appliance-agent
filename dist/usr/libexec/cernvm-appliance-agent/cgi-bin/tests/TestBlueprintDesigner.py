#!/usr/bin/python
import sys
sys.path.append(cern_vm.APP_PATH + '/cgi-bin')
sys.path.append(cern_vm.APP_PATH + '/cgi-bin/chrome')
from BlueprintDesigner import *
from HTMLPageGenerator import *
from menu import *
#to be run on the browser
def main():
    listitems=Menu([])
    for i in range(0,15):
        listitems.addItem(MenuItem('Menu Item ' + str(i+1), 'http://www.google.co.uk'))
    title = 'Test of Blueprint designer'
    content='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    contentTitle='Lorem ipsum'
    title_span=24
    leftlist=['Cern-VM']
    listspan=4
    content_span=16
    mainhtml=contain([createTitle(title, title_span), createList(leftlist,listspan), createText(contentTitle, content, content_span), str(listitems)])
    composeDocument(initialiseCss(), mainhtml)
    
main()
    
