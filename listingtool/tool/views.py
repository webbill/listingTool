from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.template import loader,Context
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.

from listingtool.ebayPythonApi import *
from listingtool.settings import AfterRangeNum,BeforeRangeNum
from django.core.paginator import Paginator, InvalidPage, EmptyPage,PageNotAnInteger
import codecs
@staff_member_required
def tool_index(request):
    try:
	page = int(request.GET.get('page', '1')[:-1])
    except:
        page = 1
    ItemAllList = ebayGetSellerList( EntriesPerPage = 100)
    ItemList = ebayGetSellerList(PageNumber = page)
    ItemsPerPage = ItemList['ItemsPerPage']['value']
    Items = ItemList['ItemArray']['Item']
    ItemsNumber = len(Items)
    #print Items
    #print ItemsPerPage
    PageItems=Paginator(ItemAllList['ItemArray']['Item'],ItemsPerPage)

    
    try:
        object = PageItems.page(page)
    except PageNotAnInteger:
        object = PageItems.page(1)
    except EmptyPage:
        object = PageItems.page(PageItems.num_pages)
    if page >= AfterRangeNum:
        page_range = PageItems.page_range[page-AfterRangeNum:page+BeforeRangeNum]
    else:
        page_range= PageItems.page_range[0:int(page)+BeforeRangeNum]
    return render_to_response('1.html',locals(),context_instance=RequestContext(request))


@staff_member_required
def AddItem(request):
    if request.method == "POST":
        Title = request.POST['Title']
        Description = request.POST['Description']
        CategoryID = request.POST['CategoryID']
        ConditionID = request.POST['ConditionID']
        StartPrice = request.POST['StartPrice']
        CategoryMappingAllowed = request.POST['CategoryMappingAllowed']
        Country = request.POST['Country']
        Currency = request.POST['Currency']
        DispatchTimeMax = request.POST['DispatchTimeMax']
        ListingDuration = request.POST['ListingDuration']
        ListingType = request.POST['ListingType'] 
        PaymentMethods = request.POST['PaymentMethods']
        PayPalEmailAddress = request.POST['PayPalEmailAddress']
        PictureDetails = 'http://pics.ebay.com/aw/pics/dot_clear.gif'#request.POST['PictureDetails']
        PostalCode = request.POST['PostalCode']
        Quantity = request.POST['Quantity']
        
        ReturnsAcceptedOption = request.POST['ReturnsAcceptedOption']
        RefundOption = request.POST['RefundOption']
        ReturnsWithinOption = request.POST['ReturnsWithinOption']
        ReturnPolicyDescription= request.POST['ReturnPolicyDescription']
        ShippingCostPaidByOption = request.POST['ShippingCostPaidByOption']
        
        ShippingType = request.POST['ShippingType']
        ShippingServicePriority = request.POST['ShippingServicePriority']
        ShippingService = request.POST['ShippingService']
        ShippingServiceCost = request.POST['ShippingServiceCost']
        Site = request.POST['Site']
        
        result = ebayAddItem(Title,
            Description,
            CategoryID,
            ConditionID,
            StartPrice,
            CategoryMappingAllowed,
            Country,
            Currency,
            DispatchTimeMax,
            ListingDuration,
            ListingType,
            PaymentMethods,
            PayPalEmailAddress,
            PictureDetails,
            PostalCode,
            Quantity,
            ReturnsAcceptedOption,#return policy
            RefundOption,
            ReturnsWithinOption,
            ReturnPolicyDescription,
            ShippingCostPaidByOption,#return policy
            ShippingType,#shipping policy
            ShippingServicePriority,
            ShippingService,
            ShippingServiceCost,#shipping policy
            Site)
        print result
        print type(result)
        if result == 'ItemIDAckTimestampDiscountReasonVersionBuildStartTimeFeesEndTime':
            return HttpResponse('Add Success.')
        return HttpResponse(result)
    else:
        return render_to_response('2.html',locals(),context_instance=RequestContext(request))