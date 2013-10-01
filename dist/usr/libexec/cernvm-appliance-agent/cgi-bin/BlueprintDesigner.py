import os
def initialiseCss():
    with open(os.environ['MY_HOME']+'/html/blueprint-css.html', 'r') as content_file:
        content = content_file.read()
    return content
    
def createList(items, span):
    div='<div class="span'+str(span)+'">\n'
    div+='<div class="notice">'
    for item in items:
        div+=str(item)+'<hr>\n'
    div+='</div>\n</div>\n'
    return div
    
def createMenuList(items, span):

    div='<div class="span'+str(span)+'">\n'
    div+='<div class="well">'
    
    div+='<ul class="nav nav-list">'
    div+='<li class="nav-header">Actions</li>'
    for item in items:
        div+=str(item) + '\n'
        div+='<li class="divider"></li>\n'
    div+='</ul></div>\n</div>\n'
    return div
        
def createNavList(items):

    div='<div class="container">\n<div class+="subnav">\n<center>'
    div+='<ul class="nav nav-pills">\n'
    for item in items:
        div+=str(item) + '\n'
        
    div+='</ul>\n</center>'
    div+='</div></div>\n'
    return div
        
def createHeader(title, span, nav_bar):
    
    div='<header class="jumbotron subhead" id="overview">\n'
    div+='<div class="container">\n<div class="span24">'  
    div+='<h1><a href="/cgi-bin/index.py"><img src="/icons/large/cernvm_logo.jpg" width="90" height="90" align="left">'+title +\
     '</a><img src="/icons/large/cern_logo.png" width="90" height="90" align="right"></h1>\n'
    div+='<p class="lead">Web appliance agent.</p>\n'
    div+='</div>\n'
    
    div+='</div>\n'
    
    div+=nav_bar
    div+='\n</header>\n'
    
    return div
    
def createText(title, body, span):
    div='<div class="span'+str(span)+'">\n'
    div+='<h2>'+title+'</h2>\n'
    div+=body
    div+='\n</div>\n'    
    return div

def contain(divs):
    
    div='<div class="container">\n'
    for d in divs:
        div+=d+'\n'
    div+='</div>\n'
    return div
    
def createLegend(text):
    return "<legend>" + text + "</legend>\n"
    
def fieldset(action, method, name, widgets, legend=None):
    form = "<form"
    if len(name) > 0:
        form +=  " name=" + name    
    if len(action) > 0:
        form += " action=" + action
    if len(method) > 0:
        form +=  " method=" + method            
    form += ">\n"
    form+='<fieldset>\n'
    if (legend != None):
        form+=legend
    form+= widgets.toHtml() + "\n</fieldset>\n</form>"
    return form

