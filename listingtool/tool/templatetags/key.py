#coding=utf-8
from django.template import Library
register = Library()
import chardet
def key(d,key_name):
    value = ""
    #print len(d)
    try:
        #print "1a"
        value = d[str(key_name)]
    except:
        #print "2a"
        try:
            #print "3"
            value = d[int(key_name)]
        except:
            #print "4"
            #print chardet.detect(key_name)
            #x = key_name.encode("utf-8")
            #print chardet.detect(x)
            #print d[(key_name)]
            value = ""     
    return value

register.filter('key', key)