from botcity.web import *
from botcity.core import *
import subprocess
from datetime import datetime
from botcity.plugins.excel import *

class Bot:
    def bot(self):
        # Read Excel Activity
        excelBot = BotExcelPlugin()
        file_or_path = "C:\\Users\\HP\\Downloads\\BankSystem\\extract.xlsx"

        dataList = excelBot.read(file_or_path=file_or_path).as_list(sheet=None)[1:]
        # Open Application Activity
        title = "BankSystem - Jornada RPA"
        executablePath = "C:\\Users\\HP\\Downloads\\BankSystem\\BankSystem.exe"
        deskBot = DesktopBot()
        deskBot.execute(executablePath)
        deskBot.connect_to_app(backend=Backend.WIN_32, timeout=60000, title=title, path=executablePath)
        popup_Window = deskBot.find_app_window(waiting_time=10000, title=title)

        # ForEach Activity
        for item in dataList:
            # If Activity
            if item[0] == "Débito":
                # Find Activity
                btnDebito = deskBot.find("Debito", x = None, y = None, width = None, height = None, threshold = None, matching = 0.8, waiting_time = 10000, best = True, grayscale = False)

                # Find And Click Activity
                deskBot.click()


            # Else Activity
            else:
                # Find Activity
                btnCredito = deskBot.find("Credito", x = None, y = None, width = None, height = None, threshold = None, matching = 0.9, waiting_time = 10000, best = True, grayscale = False)

                # Find And Click Activity
                deskBot.click()


            # Find Activity
            campoDescricao = deskBot.find("Descricao", x = None, y = None, width = None, height = None, threshold = None, matching = 0.9, waiting_time = 10000, best = True, grayscale = False)

            # Find And Click Activity
            deskBot.click()

            # Type Into Activity
            deskBot.kb_type(text=item[1], interval=0)

            # Find Activity
            campoValor = deskBot.find("Valor", x = None, y = None, width = None, height = None, threshold = None, matching = 0.9, waiting_time = 10000, best = True, grayscale = False)

            # Find And Click Activity
            deskBot.click()

            # Type Into Activity
            deskBot.kb_type(text=str(item[2]), interval=0)

            # Find Activity
            campoData = deskBot.find("Data", x = None, y = None, width = None, height = None, threshold = None, matching = 0.9, waiting_time = 10000, best = True, grayscale = False)

            # Find And Click Activity
            deskBot.click()

            # Type Into Activity
            deskBot.kb_type(text=item[3].strftime("%d/%m/%Y"), interval=0)

            # Find Activity
            btnConfirmar = deskBot.find("Confirmar", x = None, y = None, width = None, height = None, threshold = None, matching = 0.9, waiting_time = 10000, best = True, grayscale = False)

            # Find And Click Activity
            deskBot.click()



        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()