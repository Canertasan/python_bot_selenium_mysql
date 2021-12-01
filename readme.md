Before all of this, you need to install python from the official site.


Follow this link and download chromedriver for your version of chrome. And throw it in the folder with the bot
https://chromedriver.chromium.org/downloads

In the console we write separately:

pip install selenium

pip install selenium-wire

pip install aiohttp

pip install requests

pip install mysql-connector-python

2. Also, be sure to check the time with time.is 10-15 minutes before the sale. The time must be exact.


3. Also, be sure to find a random auction on the secondary market and save a link to it. The bot will open the browser and make a bid there.

Any auction will do.

You also need to prepare the money with the calculation of the bid in the auction.

Looking for the cheapest, the bot will bid on the minimum step



4. Next, open file MBbot2config.py 




ProductIdToAuction - the id of a random auction from the secondary market. The bot will automatically open the page and bid there. To calculate the balance at once, put a little more.

requestsNumber - the number of requests to buy mystery boxes. I recommend putting more than 1k requests.

saleTime - time in Unicode of the beginning of the sale. On the site you should choose your local time.

js. Number - The number of boxes you want to buy. ProductId - The product id of the sale. You can get it from the link to the sale.

path - The path to the chromedriver file you have downloaded. The path must be in the same format.

5. remember, the main 3 rules:

1- Most importantly, always try that the beginning of the sale fell on the very first requests. since every third trigger limiter and the more queries, the more often it triggers

2 - The more accounts, the more chances to buy a drop. Everyone uses bots now, you need to be faster and what would not catch limiter

3 - Leave as much money in the account, as you want boxes, if this is not the maximum. ie, if you want to buy 5 boxes, and give an account to buy 100, then the bot will buy the entire balance. as the bot sends 1500 requests to buy in this case, 5 pieces at a time.