#coding=utf-8
from django.template import Library
register = Library()
import chardet
def haskey(d,keys):
    #print d
    value = ""
    if d.has_key(key):
        return 1
    else:
        return 0
        

register.filter('haskey', haskey)