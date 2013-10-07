import sys
import os
if 'MY_HOME' not in os.environ:
    os.environ['MY_HOME']='/usr/libexec/cernvm-appliance-agent'
sys.path.append(os.environ['MY_HOME']+'/cgi-bin')
sys.path.append(os.environ['MY_HOME']+'/cgi-bin/chrome')
sys.path.append(os.environ['MY_HOME']+'/cgi-bin/toolkit')
sys.path.append(os.environ['MY_HOME']+'/etc/config')
from BlueprintDesigner import *
from menu import *
from HTMLPageGenerator import *
import cgi

#any extension should be a subclass of view. View implements by default the default views
#of the menus in the user interface. The difference of each subclass of view should be
#on the content part of the interface. 

#The interface consists of two columns, one on the left and one on the far right. In the
#middle there are the results of an action and possible options and actions.


class View(object):
    '''
    This class forms the skeleton of the main view of the system. It forms
    the menus, titles and the main display area, where the results of each
    call are placed. This is returned by the function content. The rest are
    private since the skeleton parts must remain the same through the application's
    lifecycle
    '''

    def __init__(self, actions):
        self.menu=Menu([])
        self.nav_bar=Menu([], nav=True)
        self.actions=actions
        for action in actions:
            if actions[action].secondary:
                self.menu.addItem(MenuItem(actions[action].title, actions[action].url))
            else:
                self.nav_bar.addItem(MenuItem(actions[action].title, actions[action].url))
        self.title='CernVM'
        self.titlespan=24
        self.listspan=4
        self.contentspan=16
        self.setContent('Welcome', 'This is the web interface of the CernVM')
        
    def setContent(self, title, content):
        '''
        gets a title and a content in pure html and finilises the 
        shape and look of the user interface
        '''
        self.contentTitle = title
        self.content = content
        self._view()    
    
    #def _titleView(self):
     #   return createTitle(self.title, self.titlespan)
        
    def _leftListView(self):
        with open(os.environ['MY_HOME']+"/html/information_list.html", "r") as listFile:
            data = listFile.read()    
        return data
    
    def _createNavBar(self):
        return str(self.nav_bar)    
        
    def _rightListView(self):
        return str(self.menu)
        
    def _mainWindow(self):
        return createText(self.contentTitle, self.content, self.contentspan)
    
    def _footer(self):
        return '<footer><center>\n<p>Copyright (c) CERN 2013</p>\n'+\
        '<p><time pubdate datetime="2013-09-01"></time></p>\n'+\
        '</center></footer>' 
    
    def _view(self):
        self.mainhtml=createHeader('CernVM', 16, self._createNavBar())+\
        contain([self._leftListView(),\
         self._mainWindow(), self._rightListView()])#, self._footer()])


    def output(self):
        '''
        Outputs the html in proper way to be 
        read from the browser, with the composeDocument
        function which is responsible to add the css declarations
        '''
        composeDocument(initialiseCss(), self.mainhtml)

	
