import time
import traceback
from datetime import datetime

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Automation:
    def __init__(self, HEADLESS, ON_ERROR_PROCEED, routines):
        DRIVER_PATH = Service(ChromeDriverManager().install())
        self.ON_ERROR_PROCEED = ON_ERROR_PROCEED
        self.routines = routines
        self.options = Options()
        self.options.headless = True if HEADLESS == 1 else False
        self.driver = webdriver.Chrome(service=DRIVER_PATH, options=self.options)

    def log(self, msg):
        print(msg)
        with open("log.log", "a+") as f:
            date = datetime.now()
            f.write(date.strftime("%d/%m/%Y, %H:%M:%S") + ": " + msg + "\n")

    def doAction(self, routine, i):
        try:
            if routine["action"] == "read":
                time_load = int(routine["time_load"])
                wait = int(routine["wait"])
                url = routine["url"]
                element = routine["element"]
                value_to_verify = routine["value_to_verify"]

                if url != "prev":
                    self.driver.get(url)

                time.sleep(time_load)
                element_value = self.driver.find_element(by="xpath", value=element).text
                if element_value == value_to_verify:
                    self.log(f"Step {i} was successful.")
                    time.sleep(wait)
                    return True
                else:
                    self.log(f"Step {i} was unsuccessful.")
                    if self.ON_ERROR_PROCEED == 1:
                        time.sleep(wait)
                        return True
                    else:
                        return False

            elif routine["action"] == "click":
                time_load = int(routine["time_load"])
                wait = int(routine["wait"])
                url = routine["url"]
                element = routine["element"]

                if url != "prev":
                    self.driver.get(url)

                time.sleep(time_load)
                self.driver.find_element(by="xpath", value=element).click()
                time.sleep(wait)
                self.log(f"Step {i} was successful.")

        except Exception as e:
            if self.ON_ERROR_PROCEED == 1:
                self.log(traceback.format_exc())
                return True
            else:
                return False

    def runActions(self):
        i = 1
        for routine in self.routines:
            if self.doAction(routine, i) is False:
                exit(1)
            else:
                i += 1

        self.driver.quit()


if __name__ == "__main__":
    routines = [
        {
            "time_load": "2",
            "wait": "3",
            "url": "https://example.com",
            "element": "/html/body/div/p[1]",
            "action": "read",
            "value_to_verify": "This1 domain is for use in illustrative examples in documents. You may use this domain in literature without prior coordination or asking for permission.",
        },
        {
            "time_load": "2",
            "wait":  "3",
            "url": "prev",
            "element": "/html/body/div/p[2]/a",
            "action": "click",
        }
    ]

    at = Automation(1, 0, routines)
    at.runActions()

