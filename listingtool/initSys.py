#encoding:utf-8
#do something init work.
from django.core.cache import cache
from listingtool.ebayPythonApi import *

def setCache(cache_key,data,time):
    cache.set(cache_key, data, time)
    
def setDM():
    print "setdm"
    ItemAllList = ebayGetSellerList( EntriesPerPage = 100)
    #print ItemAllList
    list =  ItemAllList['ItemArray']['Item']
    setCache('cache_dm_mc_ItemAllList',list,300) #set ItemAllList flush per 300s.
    print "setok"
def getPaDM(dmmc):
    dm = cache.get('cache_dm_mc_'+dmmc)
    print "dm",dm
    if dm is None:
	setDM()
	dm = cache.get('cache_dm_mc_'+dmmc)
    return dm

    
def flushMem(request):    
    cache._cache.flush_all()
    print "flush ok"
    initSys()
    print "set dm ok"
    return HttpResponse("ok")

setDM()

