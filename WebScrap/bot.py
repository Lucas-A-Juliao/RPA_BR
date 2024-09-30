from botcity.web import *
import subprocess
from datetime import datetime
from webscrap import Webscrap

class Bot:
    def bot(self):
        # Open Browser Activity
        webBot = WebBot()
        webBot.driver_path = "C:\\Users\\HP\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
        webBot.browser = Browser.CHROME
        webBot.headless = True
        webBot.page_load_strategy = "Normal"
        webBot.browse("https://jornadarpa.com.br/alunos/desafios/dataextractioncrm/desafios_crm-clientes.html")

        # Extract DataTable Activity
        ws = Webscrap()
        dataTable = ws.webscrap(inBot=webBot, inXPATH="/html/body/div[4]/section/div/div/div/div/div/div/div/div[2]/div/table", inLines=0,inNext="/html/body/div[4]/section/div/div/div/div/div/div/div/div[3]/div[2]/div/ul/li[5]/a")

        # Print Activity
        print(dataTable)


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()