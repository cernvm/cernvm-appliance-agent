import sys
import xml.etree.ElementTree as ET
class InputWidget(object):
    def __init__(self, wType, name, value, text, wClass = None, attribs=None):
        self.wType = wType
        self.name = name
        self.value = value
        self.text = text
        self.wClass = wClass
        self.attribs=attribs
        
    def toHtml(self):
        html=''
        if (self.wType in ['password', 'text']):
            html=self.text + '\n'
            textSet=True
        else:
            textSet=False
        html += "<input"
        if len(self.wType) > 0:
            html+= " type=" + attrib(self.wType)
        if len(self.name)>0:
            html+=" name=" + attrib(self.name) 
        if len(self.value)>0:
            html+=" value=" + attrib(self.value)

        if self.wClass != None:
            html+=" class=" + attrib(self.wClass)
        if self.attribs != None:
            html+= self.attribs
        html+=">"    
        if not textSet:
            html+=self.text
        html+='<br>'
        return html
        
class DropDownListWidget(InputWidget):
    
    def __init__(self, wType, name, value, options):
        InputWidget.__init__(self, wType, name, value, '')
        text=''
        for option in options:
            text+='<option'
            text+= ' value="'+option["value"]+'">'+option["text"]+'</option>\n'
        self.text = text
    
    def toHtml(self):
        html='<select name="'+self.name+'">\n'
        html+=self.text 
        html+='</select>\n'
        return html

class InputWidgetGroup(object):        

    def __init__(self):
        self.widgets=[]    

    def addInputWidget(self, widget):
        self.widgets.append(widget)

    def clear(self):
        self.widgets=[]
    
    def toHtml(self):
        html=""
        counter=0;
        for widget in self.widgets:
            if counter==0:
                html+=widget.toHtml()
                counter=1
            else:
                html+="<br>\n"+widget.toHtml()
        return html

def composeDocument(references, body):
    print "Content-type: text/html"
    print
    print "<html>"
    print references
    print '<body class="preview" id="top" data-spy="scroll" data-target=".subnav" data-offset="80">'
    print body
    print "</body>"
    print "</html>"

def composeXMLDocument(xml):
    print "Content-type: text/html"
    print
    print ET.tostring(xml, encoding='UTF-8')

def attrib(att):
    return '"' + att + '"'

def createForm(action, method, name, widgets):
    form = "<form"
    if len(name) > 0:
        form +=  " name=" + name    
    if len(action) > 0:
        form += " action=" + name
    if len(method) > 0:
        form +=  " method=" + method            
    form += ">\n"
    form+= widgets.toHtml() + "\n</form>\n"
    return form


def createInputWidget(wType, name, value, text):
    return InputWidget(wType, name, value, text)

def createDiv(message, divClass=None):
    if divClass == None:
        return "<div>\n" + message + "\n</div>\n"
    return '<div class="'+divClass+'">\n' + message + '\n</div>\n'
