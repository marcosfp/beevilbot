from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import telebot_avisos
import schedule
import datetime
import time
import os

def hora():
    now = datetime.datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)



def reservar_clase():
    hora()
    s3 = os.environ.get('TIMES')

    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    usernameStr = os.environ.get('usernameStr')
    passwordStr = os.environ.get('passwordStr')

    try:
        #https://marcosfp-springboot-database.herokuapp.com/login
        url_login= os.environ.get('url_login')
        browser.get((url_login))

        # fill in username and hit the next button

        username = browser.find_element(By.ID,'usr')
        username.send_keys(usernameStr)

        password = browser.find_element(By.ID,'pass')
        password.send_keys(passwordStr)


        logInButton = browser.find_element(By.XPATH,"//button[@type='submit']")
        logInButton.click()

        browser.set_page_load_timeout(10)

        #Una vez logueado cargamos todas las clases
        url_reserva = os.environ.get('url_reserva')
        browser.get((url_reserva+tomorrow_fu()))


        # Botones que contiene la palabra reservar despues del textop 9:30
        button =browser.find_elements(By.XPATH,"//p[text()='09:30 - 10:30']/ancestor::li//following::button")
        # Seleccionamos el primero que es la clase de crossfit
        button[0].click()
        telebot_avisos.enviar_mensaje("Clase Reservada")
    except Exception as e:
        telebot_avisos.enviar_mensaje("Error en el servidor")

def main():
    hora()


    schedule.every().sunday.at("00:00").do(reservar_clase)
    schedule.every().monday.at("09:30").do(reservar_clase)
    schedule.every().tuesday.at("09:30").do(reservar_clase)
    schedule.every().wednesday.at("09:30").do(reservar_clase)
    schedule.every().thursday.at("09:30").do(reservar_clase)


    while True:
        schedule.run_pending()
        time.sleep(20)


def tomorrow_fu():
    NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
    NextDay_Date_Formatted = NextDay_Date.strftime('%d-%m-%Y')  # format the date to ddmmyyyy
    return NextDay_Date_Formatted



if __name__ == "__main__":
    main()



