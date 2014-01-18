# -*- coding: utf-8 -*- 
# 用来创建一个ebay的产品页
from ebaysdk import trading
def main():
    api = trading(domain='api.sandbox.ebay.com', 
                  appid="ding18d4c-56fe-45dd-9320-d17523ee18b", devid="6a3e6a37-1763-49a2-810b-68bc6a15ee26", certid="356d53fe-7910-4247-9e99-61727cc3a4da", token="AgAAAA**AQAAAA**aAAAAA**X3bWUg**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GhC5eHowSdj6x9nY+seQ**ZH4CAA**AAMAAA**dsAoBo/3vv1yuOd4aPGBtq5ilPzSLM+3vsnOHfYuTn47JcoylH6TTyp1jH4yICQcQ6VL9FQ/0FN5YWpGy1UhM5fD5pEFIcYSUD2aECDOP55HW2KIlG4+in/NSJmp89DNj2FK1GDQzuZT3xy0pDI2yfHLW3CL1HcCIsWCNzkG0FVDJp8w5u3Nu7PVDkqQpIn5eUFMSrwyk3NalGYbPuHXkyMmS9KmGSmvrPthbhucNi1H0ihirPfQ5SaAW7O4T1r8EHfZa430655/VayOydUSovBnCnRE+WwZGg/ZRRWHIZJxbotCmD1kCH0ymE6FUl2QLm1hjkaESpKAmtFgpjhsaCVdt7vCUAt23A23P+7LBkfLsBrPwDIaeEVDEjGjFojEqliQfhq/lAcJhpO6Xi2db55fvZX/V8+7IpaHyzwtioXW8Azx8N7v+sx2mQ2spG7OWzGc+gdwW4a8lUVl3TRp0BywDqhOCXPKN94DK+Vrh6LvmzxjLvFzdWxz4YDjQ98Osyih66EfX1R0umXJPu2B3HTOpFHBtvS/TrpJzr8oOOVGgjDbyXL8yZd40PRnxi6Rkvyhj77hrGjzeowkaboLTWuqwjLTgkg9loWqQWoLjKAtVBmpasfP61bGR5y9vZhyM/b7SeHCAae1+/IJ+GB8y8d1RW022WFKZtcTiBAEvka2URU0TX7pmgEqDX1nM3a2TMlehriD8bx6WvIdEbqM7IzjFLcQ8kI+0kcOn13PIWsvHuwMHz6capQ5jYsZEu1S")
                  # api.execute('GetCategories', {
                                  # # 'CategorySiteID':0 \
                                  # 'LevelLimit':1 \
                                  # ,'DetailLevel':'ReturnAll'                                  
                                    # })
    # api.execute('GetStore', {
                                  # # 'CategorySiteID':0 \
                                  # 'LevelLimit':1 \
                                  # ,'DetailLevel':'ReturnAll'                                  
                                    # })
    # api.execute('AddItem', { \
                                  # 'Title':'LI Junjie Harry Potter and the Philosopher\'s Stone' \
                                  # , 'Description': ' This is the first book in the Harry Potter series. In excellent condition!' \
                                  # , 'PrimaryCategory':'607504'  \
                                  # , 'StartPrice' : '1.0' \
                                  # , 'CategoryMappingAllowed' : 'true' \
                                  # , 'Country' : 'US' \
                                  # , 'Currency' : 'USD' \
                                  # , 'DispatchTimeMax' : '3' \
                                  # , 'ListingDuration' : 'Days_7' \
                                  # , 'ListingType' : 'Chinese' \
                                  # , 'PaymentMethods' : 'PayPal' \
                                  # , 'PayPalEmailAddress' : 'klijunjie-facilitator@gmail.com' \
                                  # , 'PictureDetails' : 'http://pics.ebay.com/aw/pics/dot_clear.gif' \
                                  # , 'PostalCode' : '95125' \
                                  # , 'Quantity' : '1' \
                                  # , 'ReturnPolicy' : {'ReturnsAcceptedOption' : 'ReturnsAccepted' \
                                                      # , 'RefundOption' : 'MoneyBack' \
                                                      # , 'ReturnsWithinOption' : 'Days_30' \
                                                      # , 'Description' : 'If you are not satisfied, return the book for refund.' \
                                                      # , 'ShippingCostPaidByOption' : 'Buyer' \
                                                      # } \
                                  # , 'ShippingDetails' : {'ShippingType' : 'Flat' \
                                                      # , 'ShippingServiceOptions' : { 'ShippingServicePriority' : '1' \
                                                                                  # , 'ShippingService' : 'USPSMedia' \
                                                                                  # , 'ShippingServiceCost' : '2.50' \
                                                                                  # , 'ShippingCostPaidByOption' : 'Buyer' \
                                                                                  # } \
                                                        # } \
                                  # , 'Site' : 'US' \
                                    # })
    '''if True:
        api.execute('AddItem', { 'Item' : { \
                                  'Title':'Bill eBay test \'s Stone' \
                                  , 'Description': ' This is a test example.!' \
                                  , 'PrimaryCategory': {'CategoryID': '20936' }  \
                                  , 'ConditionID' : '1000' \
                                  , 'StartPrice' : '1.0' \
                                  , 'CategoryMappingAllowed' : 'true' \
                                  , 'Country' : 'US' \
                                  , 'Currency' : 'USD' \
                                  , 'DispatchTimeMax' : '3' \
                                  , 'ListingDuration' : 'Days_7' \
                                  , 'ListingType' : 'Chinese' \
                                  , 'PaymentMethods' : 'PayPal' \
                                  , 'PayPalEmailAddress' : 'dingxinzhe@gmail.com' \
                                  , 'PictureDetails' : 'http://pics.ebay.com/aw/pics/dot_clear.gif' \
                                  , 'PostalCode' : '95125' \
                                  , 'Quantity' : '1' \
                                  , 'ReturnPolicy' : {'ReturnsAcceptedOption' : 'ReturnsAccepted' \
                                                      , 'RefundOption' : 'MoneyBack' \
                                                      , 'ReturnsWithinOption' : 'Days_30' \
                                                      , 'Description' : 'If you are not satisfied, return the book for refund.' \
                                                      , 'ShippingCostPaidByOption' : 'Buyer' \
                                                      } \
                                  , 'ShippingDetails' : {'ShippingType' : 'Flat' \
                                                      , 'ShippingServiceOptions' : { 'ShippingServicePriority' : '1' \
                                                                                  , 'ShippingService' : 'USPSMedia' \
                                                                                  , 'ShippingServiceCost' : '2.50' \
                                                                                  } \
                                                        } \
                                  , 'Site' : 'US' \
                                   } })'''
    if True:
        api.execute('GetSellerList',{
            'StartTimeFrom':'2014-01-01T19:09:02.768Z',
            'StartTimeTo':'2014-01-15T23:23:02.768Z',
            'DetailLevel': 'ItemReturnAttributes',
            'Pagination':{
                'EntriesPerPage':'10',
                'PageNumber':'1'},
        })
    print api.response_dict()
    # print api.response_dict()
    # api = trading(appid="DrewLee78-f6cd-4b35-84d3-5462382213a", devid="a4b30cb6-9a6f-4d33-b26a-f281cd55fa24", certid="6ca01712-0a4c-40a3-8db7-494d5d5f6b1e", token="AgAAAA**AQAAAA**aAAAAA**Gi+fUg**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GhC5WLpgudj6x9nY+seQ**aHACAA**AAMAAA**xQkQ5qjpeV2yTLDMFAWsnkw8EnH8CQ/AAdDSE2OWz4JmxAu17TeukwhIxqL5yx+jSC+Y/3+laOk5Am9lSLxjPQk9hdRFYk2/frmP7S5617EEFsqg7N+cHP1PNWZLtyGIEV+8Ta9UaSQTYqjhOM8i1VvXKzFeXMMumkWNK35Vy2xmRAdS+57gVhWOFXTCg5QfStWCSSHZoJyoGo7uxGrKMnPDDylXXppRIAMiUmKcp7HMLZVVHWbAga05kfJ71twDBO98p7A4sYZuNffxnisQ8y0nDMOiQKO2dhxPPMpiIpjqFPk8R4oO9xGBK8oRj58xglZxzFYOJR7wxzC4ZTR7z6POjIECnfz8KElLphJuKEAIVXc/WD+vJPgeCN0BIdMAQn1OZCTFS4//5lWDuGZr+22Gq+3errpQtJf5wYRj+2ruPcBEMLvR2rlQVjy18DwVy5Qn+d0qcOvusxuRd/xcvm0ILhnQfrrUiVLrpW1WyS1xpK98GxbJMHIp/F3XuFacP7L9M8cmJQeaF3uXqwqsYbth0PzcCFbrl57imRiDQS1X4rH+a1FYV6v375th4MomjPSfvEZ/T64CGo5tKWDLskVSujqIptigdwT167ae0eDfgnp+v2H2fflMXKRTLeoa5i15XDH5Ii0YeY55p8ojEDdeHZOt8VpowRh0QDfRR8cPBbh69XCp9l4ccltj2QPL7LwoUOCVpfh7r0x8DoKTM4pRjBZWXDkxgIx5jet4RkMJtUxTO8cnsEAb0jXbqESn")
    # api.execute('GetUser', {})
    
if __name__ == '__main__':
    main()