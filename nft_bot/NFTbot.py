import json
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from seleniumwire import webdriver
import asyncio
import aiohttp
from NFTbotConfig import *
import pickle
import mysql.connector

print("Bot starting...")

DB_HOST="us-cdbr-east-04.cleardb.com"
DB_NAME="heroku_15dfd0ea68e2252"
USER_NAME="bd1d7d55ca4370"
PASSWORD="e51b2bc8"

def db_connect():
  return mysql.connector.connect(
    host=DB_HOST,
    user=USER_NAME,
    password=PASSWORD,
    database=DB_NAME
  )

mydb = db_connect()
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM users")
myresult = mycursor.fetchall()
mycursor.close()
mydb.close()
# after some time we should put our security here!
USER_ID = -1
not_logged_in = True
while not_logged_in:
    user_name = input("Please enter your username: ")
    password = input("Please enter your password: ")
    for user_info in myresult:
        if user_info[1] == user_name and user_info[2] == password:
            not_logged_in = False
            USER_ID = user_info[0]
            mydb = db_connect()
            mycursor = mydb.cursor()
            sql = "INSERT INTO logs (user_id) VALUES ({})".format(USER_ID)
            mycursor.execute(sql)
            mydb.commit()
            mycursor.close()
            mydb.close()
            print("Successfully logged in :)")

    if not_logged_in == True:
        print("Please enter your correct password and user_name!")

print()
headers = {}

def getAuctionPage():
    
    print("Trying to open AuctionPage")
    url = f'https://www.binance.com/en/nft/goods/detail?productId={productIdToAuction}&isOpen=true&isProduct=1'
    driver.get(url)
    time.sleep(2)
    driver.find_element_by_xpath('//button[text()="Place a Bid"]').click()  # buy btn

    print("CLICKED")


def clickConfirm(headers):

    time.sleep(5)

    search = driver.find_elements_by_xpath('//button[text()="Place a Bid"]')[1]
    ActionChains(driver).move_to_element(search).click().perform()

    print('CONFIRMED')

    time.sleep(3)
    
    
    for request in driver.requests:


        if str(request.url) == 'https://www.binance.com/bapi/nft/v1/private/nft/nft-trade/order-create':

            cookies = request.headers['cookie']
            csrftoken = request.headers['csrftoken']
            deviceinfo='eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjkwMCwxNDQwIiwiYXZhaWxhYmxlX3NjcmVlbl9yZXNvbHV0aW9uIjoiNzg5LDE0NDAiLCJzeXN0ZW1fdmVyc2lvbiI6Ik1hYyBPUyAxMC4xNS43IiwiYnJhbmRfbW9kZWwiOiJ1bmtub3duIiwic3lzdGVtX2xhbmciOiJ0ci1UUiIsInRpbWV6b25lIjoiR01UKzEiLCJ0aW1lem9uZU9mZnNldCI6LTYwLCJ1c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTVfNykgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC41NSBTYWZhcmkvNTM3LjM2IiwibGlzdF9wbHVnaW4iOiJQREYgVmlld2VyLENocm9tZSBQREYgVmlld2VyLENocm9taXVtIFBERiBWaWV3ZXIsTWljcm9zb2Z0IEVkZ2UgUERGIFZpZXdlcixXZWJLaXQgYnVpbHQtaW4gUERGIiwiY2FudmFzX2NvZGUiOiI0NWQzOGFhMyIsIndlYmdsX3ZlbmRvciI6IkFwcGxlIiwid2ViZ2xfcmVuZGVyZXIiOiJBcHBsZSBNMSIsImF1ZGlvIjoiMTI0LjA0MzQ0OTY4NDc1MTk4IiwicGxhdGZvcm0iOiJNYWNJbnRlbCIsIndlYl90aW1lem9uZSI6IkV1cm9wZS9CdWRhcGVzdCIsImRldmljZV9uYW1lIjoiQ2hyb21lIFY5Ni4wLjQ2NjQuNTUgKE1hYyBPUykiLCJmaW5nZXJwcmludCI6ImEwMGYxNWVkYjlkZDI5Y2Q0ZmUyN2Y5NjQ1YWI5ZDU3IiwiZGV2aWNlX2lkIjoiIiwicmVsYXRlZF9kZXZpY2VfaWRzIjoiMTYzNjU2NDQyMDk3OG90YWE0VEhJa284TUp0eTR4aHMifQ=='
            useragent='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:91.0) Gecko/20100101 Chrome/96.0.4664.45 Firefox/91.0'

            xNftCheckbotSitekey = request.headers['x-nft-checkbot-sitekey']
            xNftCheckbotToken = request.headers['x-nft-checkbot-token']
            xTraceId = request.headers['x-trace-id']
            xUiRequestTrace = request.headers['x-ui-request-trace']


            headers = {
            'Host':'www.binance.com',
            'Accept':'*/*',
            'Accept-Language':'en-US,en;q=0.5',
            'Accept-Encoding':'gzip, deflate, br',
            'clienttype':'web',
            'x-nft-checkbot-token':xNftCheckbotToken,
            'x-nft-checkbot-sitekey':xNftCheckbotSitekey,
            'x-trace-id':xTraceId,
            'x-ui-request-trace' : xUiRequestTrace,
            'content-type':'application/json',
            'cookie' : cookies,
            'csrftoken': csrftoken, 
            'device-info': deviceinfo,
            'user-agent': useragent
            }
    print("HEADERS:", headers)
    return headers

results = []
status = []
url = 'https://www.binance.com/bapi/nft/v1/private/nft/nft-trade/order-create'


def get_tasks(session):
    tasks = []
    js.update({"tradeType":0})
    print("Making Request Started:", time.time())
    for i in range(0,requestsNumber):
        tasks.append(asyncio.create_task(session.post(url, data = json.dumps(js), ssl=False)))
    print("Finishing Request Started:", time.time())
    print(len(tasks))
    return tasks

async def get_symbols(headers):
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = get_tasks(session)
        print(time.time())
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.text())
            status.append(response.status)


def startSsc(headers):
    asyncio.get_event_loop().run_until_complete(get_symbols(headers))

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument('no-sandbox')
driver = webdriver.Chrome(executable_path=path, options=chrome_options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})


driver.maximize_window()
# print("trying to get binance nft website...(60 seconds waiting)")
# driver.get("https://binance.com/en/nft")
# if os.path.isfile('./cookies.pkl'):
#   print("loading cookies...")
#   cookies = pickle.load(open("cookies.pkl", "rb"))
#   for cookie in cookies:
#       driver.add_cookie(cookie)
#   print("cookies loaded, if you have any :)")
print("trying to get binance nft website...")
driver.get("https://binance.com/en/nft")

a = input('Login first then press Enter: ')

getAuctionPage()

print('hi')

rqStart = 0
rqStop = 0
while True:
    ts = time.time()
    if saleTime>ts:
        print(f'{saleTime-ts} - seconds left')
    if saleTime-ts < 15.0:
        break
rqStart=time.time()

headers = clickConfirm({})

while True:
    ts = time.time()
    if saleTime>ts:
        print(f'{saleTime-ts} - seconds left')
    if saleTime<ts:
        startSsc(headers)
        break

counter_block = 0
rqStop = time.time()
for i in range(len(results)):
    if len(results[i])>250:
        print('status:', status[i], 'blocked')
        counter_block += 1
    else:
        print('status:', status[i], 'result:', results[i])

print("Number of blocked requests:", counter_block)
print("Number of others requests:", requestsNumber - counter_block)

driver.quit()
