"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/web/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

from webdriver_manager.chrome import ChromeDriverManager

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()
    
    # Uncomment to set the WebDriver path
    # bot.driver_path = "<path to your WebDriver binary>"

    # Opens the BotCity website.
    bot.browse("https://sistemas1.sefaz.ma.gov.br/portalsefaz/jsp/principal/principal.jsf")

    # Implement here your logic...
    bot.maximize_window()
    bot.sleep(3000)
    if not bot.find( "bttn_fechar", matching=0.97, waiting_time=10000):
        not_found("bttn_fechar")
    bot.click()
    redirecionamento= bot.find_element(selector="/html/body/div[2]/div/form/div[2]/div[2]/div[1]/div/div[1]/a[2]",by=By.XPATH)
    redirecionamento.click()
    redirecionamento2= bot.find_element(selector="/html/body/div[2]/div/form/div/ul/li[4]/a",by=By.XPATH)
    redirecionamento2.click()
    redirecionamento3= bot.find_element(selector="/html/body/div[2]/div/form/div/div[2]/div/span[1]/span/div/ul/li[6]/a",by=By.XPATH)
    redirecionamento3.click()
    iframe = bot.find_element('/html/frameset/frame', By.XPATH)
    bot.enter_iframe(iframe)

    #IE empresa
    ie_empresa='0101010'
    bot.find_element('//*[@id="form1:j_id6_body"]/table[1]/tbody/tr[1]/td[2]/input', By.XPATH).send_keys(str(ie_empresa))
    
    #CPF Sócio
    socio='01010101'
    bot.find_element('//*[@id="form1:j_id6_body"]/table[1]/tbody/tr[2]/td[2]/input', By.XPATH).send_keys(str(socio))
    
    #Último Protocolo DIEF
    dief='01010101'
    bot.find_element('//*[@id="form1:j_id6_body"]/table[1]/tbody/tr[3]/td[2]/input', By.XPATH).send_keys(str(dief))

    #Data Inicial
    data_inicial='01/08/2024'
    bot.execute_javascript(f"""
        var campo = document.evaluate('//*[@id="form1:dtIniInputDate"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        campo.value = '{data_inicial}';
        campo.dispatchEvent(new Event('input'));
        campo.dispatchEvent(new Event('change'));
        """)
    bot.sleep(2000)
    #Data Final
    data_final='07/08/2024'
    bot.execute_javascript(f"""
        var campo = document.evaluate('//*[@id="form1:dtFinInputDate"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        campo.value = '{data_final}';
        campo.dispatchEvent(new Event('input'));
        campo.dispatchEvent(new Event('change'));
        """)
    
    bot.sleep(2000)

    # Limpar formulário
    bot.find_element('//*[@id="form1:j_id6_body"]/table[4]/tbody/tr/td[1]/input', By.XPATH).click()
    bot.wait(10000)
    # input()
    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()









