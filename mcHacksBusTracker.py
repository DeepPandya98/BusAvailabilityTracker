import os
import cv2
import json
import time
import datetime
import pytesseract
from selenium import webdriver
from twilio.rest import Client


class TicketTracker():
    def __init__(self):
        self.loadConfig()

        # Configure tesseract path
        pytesseract.pytesseract.tesseract_cmd = self.tesseractPath

        # Configure selenium chrome webdriver
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('log-level=3')
        self.driver = webdriver.Chrome(
            'chromedriver/chromedriver.exe', options=options)

        # Configure Twilio client
        account_sid = self.twilioConfig['ACCOUNT_SID']
        auth_token = self.twilioConfig['AUTH_TOKEN']
        self.client = Client(account_sid, auth_token)

    def loadConfig(self):
        with open('config.json', 'r') as f:
            config = json.load(f)

        self.twilioConfig = config['TWILIO']
        self.tesseractPath = config['TESSERACT_FILEPATH']
        self.recipients = config['NOTIF_RECIPIENTS']

    def takeScreenShot(self):
        self.driver.get('https://bus.mchacks.ca/')
        self.driver.save_screenshot("./screenshot.png")
        self.checkAvailable()

    def checkAvailable(self):
        img = cv2.imread('./screenshot.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        screenText = pytesseract.image_to_string(img)
        if("soldout" not in "".join(screenText.lower().split())):
            # Tickets available
            print("Tickets Available")
            self.sendText("TICKETS AVAILABLE, GO BUY NOW!!!!!")
        else:
            print("Sold out")

    def sendText(self, msg):
        for number in self.recipients:
            message = self.client.messages \
                .create(
                    body=msg,
                    from_=self.twilioConfig['NUMBER'],
                    to=number)

    def runLoop(self):
        while(True):
            print(datetime.datetime.now())
            self.takeScreenShot()
            time.sleep(300)

        self.driver.close()


test = TicketTracker()
test.runLoop()
