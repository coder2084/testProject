import requests
import json
import os
import xlrd

game = '/game/fifa17'

myUrls = {'getCredits': '/user/credits',
          'buyPack': '/purchased/items',
          'clubStatsNewCards': '/club/stats/newcards',
          'getActiveSquad': '/squad/active?active=true',
          'getSquadList': '/squad/list',
          'getAvPacks':'/store/purchasegroup/all?ppInfo=true',
          'getUserInfo': '/user',
          'getUserData': '/userdata',
          'userHubData': '/clientdata/userHubData',
          'hubInfo': '/hub',
          'getClubStaff': '/club/stats/staff',          
          'moveItem': '/item',
          'searchClub': '/club',
          'trMarketSearch': '/transfermarket?',
          'clubUser': '/clubUser',
          'getManagerQuest': '/clientdata/managerquest',
          'getPileData': '/clientdata/pileSize',
          'getSettings': '/settings',
          'resetMatch': '/match/reset',          
          'getTOTWData': '/clientdata/totw',
          'getTradePile': '/tradePile',
          'auctionHouse': '/auctionhouse',
          'getSuggestPrice': '/marketdata/item/pricelimits?itemIdList=',
          'getTradePileCount': '/tradePile/counts',
          'relistItems': '/auctionhouse/relist',
          'getTourList': '/tournament/list?active=true&count=10',
          'activeTourIdList': '/tournament/user/list',
          'moveCardByRes': '/item/resource',
          'userMassInfo': '/usermassInfo'}

for key, value in myUrls.items():
    myUrls[key] = serverUrl + game + value

def PrintTradePile():
    print('Getting trade pile')
    

print('Working from ' , os.getcwd())
url = 'https://utas.external.s2.fut.ea.com/ut/game/fifa17/usermassinfo'
header = {'X-UT-PHISHING-TOKEN': '8724247154698502146', 'X-UT-SID': 'ce9173b5-9289-4fc6-be4c-ea9e0ae8b094', 'X-HTTP-Method-Override': 'GET'}
r = requests.post(url,headers=header)
print('Status code: {0} \n' .format(r.status_code))
j = json.loads(r.text)
if 'squad' in j.keys():
    squad = j['squad']['players']
    for item in squad:
        playerId = item['itemData']['assetId']
        print (playerId)
else:
    print('Nu exist squad')
