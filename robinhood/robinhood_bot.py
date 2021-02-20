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
        self.driver.get('https://www.tradingview.com/#signin')
        sleep(2)

        #enter in email and pass
        login_btn = self.driver.find_element_by_xpath('//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div/span')        
        login_btn.click()
        sleep(1)
        #email_in = self.driver.find_element_by_xpath('/html/body/div[11]/div/div[2]/div/div/div/div/div/div/form/div[1]/div[1]/input')
        #email_in.send_keys('')
        sleep(15)

    def login_robinhood(self):
        #rh login
        self.driver.get('https://robinhood.com/login')
        sleep(2)

        #enter in email 
        email_in = self.driver.find_element_by_xpath('//*[@id="react_root"]/div[1]/div[2]/div/div/div/div/div/form/div/div/div[1]/label/div[2]/input')
        email_in.send_keys('youremailhere@gmail.com')
        sleep(15)

    def get_tv_data(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(20)
        #click on list of trades button
        try:
            list_trades_btn = self.driver.find_element_by_xpath('//*[@id="bottom-area"]/div[4]/div[1]/div[5]/ul/li[3]')
            list_trades_btn.click()
        except Exception:
            #your personal tradingview link here
            bot.driver.get('https://www.tradingview.com/chart/PERSONAL LINK HERE/')
            sleep(20)
            list_trades_btn = self.driver.find_element_by_xpath('//*[@id="bottom-area"]/div[4]/div[1]/div[5]/ul/li[3]')
            list_trades_btn.click()
            sleep(3)
        sleep(3)

        #scroll down to the last trade
        try:
            bottom_of_trade = self.driver.find_element_by_xpath('//*[@id="bottom-area"]/div[4]/div[2]/div/div')
        except Exception:
            print("The bottom of trade element is not working!")
        sleep(3)
        try:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", bottom_of_trade)
        except Exception as e:
            print("Scrolling down did not work! Refreshing page")
            print(e)
            bot.driver.get('https://www.tradingview.com/chart/PERSONAL LINK HERE/')
            bot.get_tv_data()
        sleep(3)
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

    def buy_rh(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        sleep(1)
        self.driver.get('https://robinhood.com/')
        portfolio = self.driver.find_element_by_xpath('//*[@id="react_root"]/main/div[2]/div/div/div/div/main/div/div[1]/section[1]/header/div[1]/h1/span/span/div').text
        portfolio = portfolio.replace(',', '')
        portfolio = float(portfolio[1:])
        #stock of your choice
        self.driver.get('https://robinhood.com/stocks/GME')
        current_stock_price = self.driver.find_element_by_xpath('//*[@id="react_root"]/main/div[2]/div/div/div/div/main/div[2]/div[1]/div/section[1]/header/div[1]/h1/span/span/div').text
        current_stock_price = float(current_stock_price[1:]) 
        sleep(1)
        shares = int(portfolio/current_stock_price)
        buy_tab = self.driver.find_element_by_xpath('//*[@id="react_root"]/main/div[2]/div/div/div/div/main/div[2]/div[2]/div/div[1]/form/div[1]/div/div[1]/div/div/div[1]')
        buy_tab.click()
        shares_box = self.driver.find_element_by_xpath('//*[@id="react_root"]/main/div[2]/div/div/div/div/main/div[2]/div[2]/div/div[1]/form/div[2]/div/div[1]/div/div/div/input')
        shares_box.send_keys(shares)
        review_order_btn = self.driver.find_element_by_xpath('//*[@id="react_root"]/main/div[2]/div/div/div/div/main/div/div[2]/div/div[1]/form/div[3]/div/div[2]/div[1]/div/button')
        review_order_btn.click()
        sleep(5)
        buy_rh_btn = self.driver.find_element_by_xpath('//*[@id="react_root"]/main/div[2]/div/div/div/div/main/div[2]/div[2]/div/div[1]/form/div[3]/div/div[2]/div[1]/div/button')
        buy_rh_btn.click()
        sleep(5)
        done_btn = self.driver.find_element_by_xpath('//*[@id="react_root"]/main/div[2]/div/div/div/div/main/div[2]/div[2]/div/div[1]/div/div[3]/div/button')
        done_btn.click()

    def sell_rh(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        #stock of your choice
        self.driver.get('https://robinhood.com/stocks/GME')
        sleep(1)
        sell_tab = self.driver.find_element_by_xpath('//*[@id="react_root"]/main/div[2]/div/div/div/div/main/div[2]/div[2]/div/div[1]/form/div[1]/div/div[1]/div/div/div[2]')
        sell_tab.click()
        sleep(1)
        sell_all = self.driver.find_element_by_xpath('//*[@id="react_root"]/main/div[2]/div/div/div/div/main/div[2]/div[2]/div/div[1]/form/footer/button/span')
        sell_all.click()
        sleep(1)
        order_btn = self.driver.find_element_by_xpath('//*[@id="react_root"]/main/div[2]/div/div/div/div/main/div[2]/div[2]/div/div[1]/form/div[3]/div/div[2]/div[1]/div/button')
        order_btn.click()
        sleep(5)
        sell_btn = self.driver.find_element_by_xpath('//*[@id="react_root"]/main/div[2]/div/div/div/div/main/div[2]/div[2]/div/div[1]/form/div[3]/div/div[2]/div[1]/div/button')
        sell_btn.click()
        sleep(5)
        done_btn = self.driver.find_element_by_xpath('//*[@id="react_root"]/main/div[2]/div/div/div/div/main/div[2]/div[2]/div/div[1]/div/div[3]/div/button')
        done_btn.click()
        sleep(1)

bot = frama_bot()
bot.login_tv()
sleep(3)
bot.driver.execute_script("window.open('');")
bot.driver.switch_to.window(bot.driver.window_handles[1])
bot.login_robinhood()
sleep(3)
bot.driver.switch_to.window(bot.driver.window_handles[0])
sleep(3)
bot.driver.get('https://www.tradingview.com/chart/PERSONAL LINK HERE/')
bot.get_tv_data()
trade_num_when_program_run = bot.current_trade_num
print("Initial trade number: ", end = '')
print(trade_num_when_program_run)

while True:
    if (datetime.datetime.now().hour == 9 and datetime.datetime.now().minute == 30) or (datetime.datetime.now().hour == 15 and datetime.datetime.now().minute == 30) or (datetime.datetime.now().hour == 15 and datetime.datetime.now().minute == 35) or (datetime.datetime.now().hour == 9 and datetime.datetime.now().minute == 35):
        print("############################")
        sleep(30)
        print(datetime.datetime.now())
        bot.get_tv_data()
        print("Current trade number: ", end = '')
        print(bot.current_trade_num)
        if bot.current_trade_num < trade_num_when_program_run:
            print("Got the incorrect trade number. Refreshing page")
            bot.driver.switch_to.window(bot.driver.window_handles[0])
            sleep(1)
            bot.driver.get('https://www.tradingview.com/chart/luaUJAKN/')
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
                bot.buy_rh()
                print("Just bought GME on ", end = '')
                print(bot.trade_date)
                print("at ", end = '')
                print(bot.trade_price)
            if bot.entry_comment == "Entry Short":
                bot.sell_rh()
                print("Just sold GME on ", end = '')
                print(bot.trade_date)
                print("at ", end = '')
                print(bot.trade_price)
                
        sleep(33)