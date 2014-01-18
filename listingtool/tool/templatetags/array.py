#coding=utf-8
from django.template import Library
register = Library()
import chardet
def array(d,number):
    #print "d",d
    value = ""
    #print len(d)
    try:
        #print "1a"
        value = d[int(number)]
    except:
        value = d[0]    
    return value

register.filter('array', array)