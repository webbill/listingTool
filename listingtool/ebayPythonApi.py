# -*- coding: utf-8 -*- 
# 用来创建一个ebay的产品页
from ebaysdk import trading
import httplib, ConfigParser, urlparse
from xml.dom.minidom import parse, parseString
import datetime

eBayDomain = 'api.sandbox.ebay.com'
eBayAppId ="ding18d4c-56fe-45dd-9320-d17523ee18b"
eBayDevId="6a3e6a37-1763-49a2-810b-68bc6a15ee26"
eBayCertId="356d53fe-7910-4247-9e99-61727cc3a4da"
eBayToken="AgAAAA**AQAAAA**aAAAAA**X3bWUg**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GhC5eHowSdj6x9nY+seQ**ZH4CAA**AAMAAA**dsAoBo/3vv1yuOd4aPGBtq5ilPzSLM+3vsnOHfYuTn47JcoylH6TTyp1jH4yICQcQ6VL9FQ/0FN5YWpGy1UhM5fD5pEFIcYSUD2aECDOP55HW2KIlG4+in/NSJmp89DNj2FK1GDQzuZT3xy0pDI2yfHLW3CL1HcCIsWCNzkG0FVDJp8w5u3Nu7PVDkqQpIn5eUFMSrwyk3NalGYbPuHXkyMmS9KmGSmvrPthbhucNi1H0ihirPfQ5SaAW7O4T1r8EHfZa430655/VayOydUSovBnCnRE+WwZGg/ZRRWHIZJxbotCmD1kCH0ymE6FUl2QLm1hjkaESpKAmtFgpjhsaCVdt7vCUAt23A23P+7LBkfLsBrPwDIaeEVDEjGjFojEqliQfhq/lAcJhpO6Xi2db55fvZX/V8+7IpaHyzwtioXW8Azx8N7v+sx2mQ2spG7OWzGc+gdwW4a8lUVl3TRp0BywDqhOCXPKN94DK+Vrh6LvmzxjLvFzdWxz4YDjQ98Osyih66EfX1R0umXJPu2B3HTOpFHBtvS/TrpJzr8oOOVGgjDbyXL8yZd40PRnxi6Rkvyhj77hrGjzeowkaboLTWuqwjLTgkg9loWqQWoLjKAtVBmpasfP61bGR5y9vZhyM/b7SeHCAae1+/IJ+GB8y8d1RW022WFKZtcTiBAEvka2URU0TX7pmgEqDX1nM3a2TMlehriD8bx6WvIdEbqM7IzjFLcQ8kI+0kcOn13PIWsvHuwMHz6capQ5jYsZEu1S"


api = trading(domain=eBayDomain,
              appid=eBayAppId,
              devid=eBayDevId,
              certid=eBayCertId,
              token=eBayToken)


    
def ebayGetSellerList(DetailLevel = 'ReturnAll',EntriesPerPage = '10' ,PageNumber = '1'):
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    tomorrow = today + oneday
    now = str(datetime.datetime.now())
    StartTimeTo = str(tomorrow)+"T"+now[11:23]+"Z"
    #print StartTimeTo
    api.execute('GetSellerList',{
            'StartTimeFrom':'2014-01-01T19:09:02.768Z',
            'StartTimeTo':StartTimeTo,#'2014-01-15T23:23:02.768Z',
            'DetailLevel': DetailLevel,#'ReturnAll',#'ItemReturnAttributes',
            'Pagination':{
                'EntriesPerPage':EntriesPerPage,
                'PageNumber':PageNumber},
        })
    return api.response_dict()
    #return api.response_content()


    
def ebayGetCategories():
    api.execute('GetCategories', {
              'CategorySiteID':0,
             'LevelLimit':1,
             'DetailLevel':'ReturnAll',                                  
             })


def ebayGetStore():
    api.execute('GetStore', {
              'CategorySiteID':0,
              'LevelLimit':1,
              'DetailLevel':'ReturnAll'                                  
               })

def ebayAddItem(Title,
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
            Site,
            ):
    '''item = { 'Item' : { \
                                  'Title':Title \
                                  , 'Description':Description \
                                  , 'PrimaryCategory': {'CategoryID': CategoryID }  \
                                  , 'ConditionID' :  ConditionID\
                                  , 'StartPrice' : StartPrice \
                                  , 'CategoryMappingAllowed' : CategoryMappingAllowed \
                                  , 'Country' : Country \
                                  , 'Currency' : Currency \
                                  , 'DispatchTimeMax' : DispatchTimeMax  \
                                  , 'ListingDuration' :  ListingDuration \
                                  , 'ListingType' : ListingType \
                                  , 'PaymentMethods' : PaymentMethods \
                                  , 'PayPalEmailAddress' : PayPalEmailAddress \
                                  , 'PictureDetails' : PictureDetails \
                                  , 'PostalCode' : PostalCode \
                                  , 'Quantity' : PostalCode \
                                  , 'ReturnPolicy' : {'ReturnsAcceptedOption' : ReturnsAcceptedOption \
                                                      , 'RefundOption' : RefundOption \
                                                      , 'ReturnsWithinOption' : ReturnsWithinOption \
                                                      , 'Description' : ReturnPolicyDescription \
                                                      , 'ShippingCostPaidByOption' : ShippingCostPaidByOption \
                                                      } \
                                  , 'ShippingDetails' : {'ShippingType' : ShippingType \
                                                      , 'ShippingServiceOptions' : { 'ShippingServicePriority' : ShippingServicePriority \
                                                                                  , 'ShippingService' : ShippingService \
                                                                                  , 'ShippingServiceCost' : ShippingServiceCost \
                                                                                  } \
                                                        } \
                                  , 'Site' : Site \
                                   } }'''
    #print item
    api.execute('AddItem', { 'Item' : { \
                                  'Title':Title \
                                  , 'Description':Description \
                                  , 'PrimaryCategory': {'CategoryID': CategoryID }  \
                                  , 'ConditionID' :  ConditionID\
                                  , 'StartPrice' : StartPrice \
                                  , 'CategoryMappingAllowed' : CategoryMappingAllowed \
                                  , 'Country' : Country \
                                  , 'Currency' : Currency \
                                  , 'DispatchTimeMax' : DispatchTimeMax  \
                                  , 'ListingDuration' :  ListingDuration \
                                  , 'ListingType' : ListingType \
                                  , 'PaymentMethods' : PaymentMethods \
                                  , 'PayPalEmailAddress' : PayPalEmailAddress \
                                  , 'PictureDetails' : PictureDetails \
                                  , 'PostalCode' : PostalCode \
                                  , 'Quantity' : Quantity \
                                  , 'ReturnPolicy' : {'ReturnsAcceptedOption' : ReturnsAcceptedOption \
                                                      , 'RefundOption' : RefundOption \
                                                      , 'ReturnsWithinOption' : ReturnsWithinOption \
                                                      , 'Description' : ReturnPolicyDescription \
                                                      , 'ShippingCostPaidByOption' : ShippingCostPaidByOption \
                                                      } \
                                  , 'ShippingDetails' : {'ShippingType' : ShippingType \
                                                      , 'ShippingServiceOptions' : { 'ShippingServicePriority' : ShippingServicePriority \
                                                                                  , 'ShippingService' : ShippingService \
                                                                                  , 'ShippingServiceCost' : ShippingServiceCost \
                                                                                  } \
                                                        } \
                                  , 'Site' : Site \
                                   } })
    print 'api:',api.response_dict()
    return api.response_dict()
    
