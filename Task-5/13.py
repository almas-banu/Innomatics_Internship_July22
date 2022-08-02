# Detect HTML Tags,Attributes and Attribute Values

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print(tag)
        [print('-> {} > {}'.format(*i)) for i in attrs ]
        
n = int(input())
html = "\n".join([input() for j in range(n)])
parser = MyHTMLParser()
parser.feed(html)
parser.close()