from botcity.core import *
import subprocess
from datetime import datetime
from botcity.plugins.excel import *

class Bot:
    def bot(self):
        # Read Excel Activity
        excelBot = BotExcelPlugin()
        file_or_path = "C:\\Users\\HP\\Downloads\\BankSystem\\extract.xlsx"

        dataList = excelBot.read(file_or_path=file_or_path).as_list(sheet="extrato")[1:]
        # Open Application Activity
        title = "BankSystem - Jornada RPA"
        executablePath = "C:\\Users\\HP\\Downloads\\BankSystem\\BankSystem.exe"
        deskBot = DesktopBot()
        deskBot.execute(executablePath)
        deskBot.connect_to_app(backend=Backend.UIA, timeout=60000, title=title, path=executablePath)
        popup_Window = deskBot.find_app_window(waiting_time=10000, title=title)

        # Find App Element Activity
        btDebito = deskBot.find_app_element(from_parent_window=popup_Window, waiting_time=10000, auto_id="rbDebito",)

        # Find App Element Activity
        btCredito = deskBot.find_app_element(from_parent_window=popup_Window, waiting_time=10000, auto_id="rbCredito",)

        # Find App Element Activity
        txtDesc = deskBot.find_app_element(from_parent_window=popup_Window, waiting_time=10000, auto_id="txtDescricao",)

        # Find App Element Activity
        txtValor = deskBot.find_app_element(from_parent_window=popup_Window, waiting_time=10000, auto_id="txtValor",)

        # Find App Element Activity
        txtData = deskBot.find_app_element(from_parent_window=popup_Window, waiting_time=10000, auto_id="PART_TextBox",)

        # Find App Element Activity
        btConfirmar = deskBot.find_app_element(from_parent_window=popup_Window, waiting_time=10000, auto_id="btnConfirmar",)

        # ForEach Activity
        for item in dataList:
            # If Activity
            if item[0] == "Débito":
                # Find And Click Activity
                btDebito.click()


            # Else Activity
            else:
                # Find And Click Activity
                btCredito.click()


            # Type Into Activity
            txtDesc.type_keys(keys=item[1], with_spaces=True)

            # Type Into Activity
            txtValor.type_keys(keys=item[2], with_spaces=True)

            # Type Into Activity
            txtData.type_keys(keys=item[3], with_spaces=True)

            # Find And Click Activity
            btConfirmar.click()


        # Wait Activity
        deskBot.wait(5000)


        return
if __name__ == '__main__':
    bot = Bot()
    bot.bot()