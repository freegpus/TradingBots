from selenium import webdriver
from time import sleep
import time
import datetime 

class frama_bot():

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.entry_comment = ""
        self.trade_price = 0.0
        self.current_trade_num = 0
        self.trade_date = ""
    
    def login_tv(self):
        #tradingview login
        self.driver.get('https://www.tradingview.com/')
        sleep(2)

        #enter in email and pass
        login_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div[3]/a')
        login_btn.click()
        sleep(1)
        #email_in = self.driver.find_element_by_xpath('//*[@id="signin-form"]/div[1]/div[1]/input')
        sleep(15)

    def login_coinbase(self):
        #coinbase login
        self.driver.get('https://pro.coinbase.com/oauth_redirect')
        sleep(2)

        #enter in email 
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('youremailhere@gmail.com')
        sleep(25)

    def get_tv_data(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(10)
        #click on list of trades button
        try:
            list_trades_btn = self.driver.find_element_by_xpath('//*[@id="bottom-area"]/div[4]/div[1]/div[5]/ul/li[3]')
            list_trades_btn.click()
        except Exception:
            bot.driver.get('https://www.tradingview.com/chart/your personal link/')
            sleep(20)
            list_trades_btn = self.driver.find_element_by_xpath('//*[@id="bottom-area"]/div[4]/div[1]/div[5]/ul/li[3]')
            list_trades_btn.click()
            sleep(3)
        sleep(2)
        #scroll down to the last trade
        try:
            bottom_of_trade = self.driver.find_element_by_xpath('//*[@id="bottom-area"]/div[4]/div[2]/div/div')
        except Exception:
            print("The bottom of trade element is not working!")
        sleep(2)
        try:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", bottom_of_trade)
        except Exception as e:
            print("Scrolling down did not work! Refreshing page")
            print(e)
            bot.driver.get('https://www.tradingview.com/chart/your personal link/')
            bot.get_tv_data()
        sleep(2)
        try:
            self.entry_comment = self.driver.find_element_by_xpath('//*[@id="bottom-area"]/div[4]/div[2]/div/div/div/div/table/tbody[6]/tr[1]/td[2]').text
        except Exception:
            self.entry_comment = self.driver.find_element_by_xpath('//*[@id="bottom-area"]/div[4]/div[2]/div/div/div/div/table/tbody[5]/tr[1]/td[2]').text
        try:
            self.trade_price = float(self.driver.find_element_by_xpath('//*[@id="bottom-area"]/div[4]/div[2]/div/div/div/div/table/tbody[6]/tr[1]/td[5]').text)
        except Exception:
            self.trade_price = float(self.driver.find_element_by_xpath('//*[@id="bottom-area"]/div[4]/div[2]/div/div/div/div/table/tbody[5]/tr[1]/td[5]').text)
        try:
            self.current_trade_num = int(self.driver.find_element_by_xpath('//*[@id="bottom-area"]/div[4]/div[2]/div/div/div/div/table/tbody[6]/tr[1]/td[1]').text)
        except Exception:
            self.current_trade_num = int(self.driver.find_element_by_xpath('//*[@id="bottom-area"]/div[4]/div[2]/div/div/div/div/table/tbody[5]/tr[1]/td[1]').text)
        try:
            self.trade_date = self.driver.find_element_by_xpath('//*[@id="bottom-area"]/div[4]/div[2]/div/div/div/div/table/tbody[6]/tr[1]/td[4]').text
        except Exception:
            self.trade_date = self.driver.find_element_by_xpath('//*[@id="bottom-area"]/div[4]/div[2]/div/div/div/div/table/tbody[5]/tr[1]/td[4]').text

    def buy_eth(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(1)
        try:
            usd_btn = self.driver.find_element_by_xpath('//*[@id="page_content"]/div/div/div[3]/div[2]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/span')
        except Exception:
            print("USD element is not working! Retrying new element")
            usd_btn = self.driver.find_element_by_xpath('//*[@id="page_content"]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/span')
        try:
            usd_btn.click()
        except Exception:
            print("clicking on USD did not work")
        sleep(1)
        try:
            buy_btn = self.driver.find_element_by_xpath('//*[@id="page_content"]/div/div/div[3]/div[2]/div/div[1]/div/div/div/div/div[3]/div/div[2]/form/div[3]/div[4]')
        except Exception:
            print("buy btn element isn't working, reassigning element")
            buy_btn = self.driver.find_element_by_xpath('//*[@id="page_content"]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[3]/div/div[2]/form/div[3]/div[4]') 
        try:
            buy_btn.click()
            sleep(2)
        except Exception:
            print("buying button didn't work!")

    def sell_eth(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(1)
        try:
            eth_btn = self.driver.find_element_by_xpath('//*[@id="page_content"]/div/div/div[3]/div[2]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/span')
        except Exception:
            print("eth btn element isn't working! Retrying new element")
            eth_btn = self.driver.find_element_by_xpath('//*[@id="page_content"]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/span')
        try:
            eth_btn.click()
        except Exception:
            print("the eth button itself didn't work!")
        sleep(1)
        try:
            sell_btn = self.driver.find_element_by_xpath('//*[@id="page_content"]/div/div/div[3]/div[2]/div/div[1]/div/div/div/div/div[3]/div/div[2]/form/div[3]/div[4]')
        except Exception:
            print("sell btn element didn't work! reassigning element")
            sell_btn = self.driver.find_element_by_xpath('//*[@id="page_content"]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[3]/div/div[2]/form/div[3]/div[4]')
        try:
            sell_btn.click()
            sleep(2)
        except Exception:
            print("selling button didn't work!")

    def wake_up_cb(self):
        print("Inactivity click for coinbase occured lil bitch on: ", end = '')
        print(datetime.datetime.now())
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(1)
        market_btn = self.driver.find_element_by_xpath('//*[@id="page_content"]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[3]/div/div[2]/form/div[2]/div/div/div[1]/span[1]')
        market_btn.click()

bot = frama_bot()
bot.login_tv()
sleep(3)
bot.driver.execute_script("window.open('');")
bot.driver.switch_to.window(bot.driver.window_handles[1])
bot.login_coinbase()
bot.driver.get('https://pro.coinbase.com/trade/ETH-USD')
sleep(3)
bot.driver.switch_to.window(bot.driver.window_handles[0])
sleep(3)
bot.driver.get('https://www.tradingview.com/chart/your personal link/')
bot.get_tv_data()
trade_num_when_program_run = bot.current_trade_num
print("Initial trade number: ", end = '')
print(trade_num_when_program_run)

while True:
    
    if (((datetime.datetime.now().hour % 12 == 0) and (datetime.datetime.now().minute == 0))) or (datetime.datetime.now().hour % 12 == 0 and datetime.datetime.now().minute == 5):
        sleep(15)
        bot.driver.switch_to.window(bot.driver.window_handles[0])
        bot.driver.get('https://www.tradingview.com/chart/your personal link/')      
        sleep(30)
        print("############################")
        print(datetime.datetime.now())
        bot.get_tv_data()
        print("Current trade number: ", end = '')
        print(bot.current_trade_num)
        if bot.current_trade_num < trade_num_when_program_run:
            print("Got the incorrect trade number. Refreshing page")
            bot.driver.switch_to.window(bot.driver.window_handles[0])
            sleep(1)
            bot.driver.get('https://www.tradingview.com/chart/your personal link/')
            sleep(10)
            print("############################")
            print(datetime.datetime.now())
            bot.get_tv_data()
            print("Current trade number: ", end = '')
            print(bot.current_trade_num)
        if bot.current_trade_num > trade_num_when_program_run:
            trade_num_when_program_run = bot.current_trade_num
            print(bot.entry_comment)
            if bot.entry_comment == "Entry Long":
                print("Time trade initiated: ", end = '')
                print(datetime.datetime.now())
                bot.buy_eth()
                bot.driver.get('https://pro.coinbase.com/trade/ETH-USD')
                print("Just bought Eth on ", end = '')
                print(bot.trade_date)
                print("at ", end = '')
                print(bot.trade_price)
            if bot.entry_comment == "Entry Short":
                print("Time trade initiated: ", end = '')
                print(datetime.datetime.now())
                bot.sell_eth()
                bot.driver.get('https://pro.coinbase.com/trade/ETH-USD')
                print("Just sold Eth on ", end = '')
                print(bot.trade_date)
                print("at ", end = '')
                print(bot.trade_price)
                
        sleep(33)