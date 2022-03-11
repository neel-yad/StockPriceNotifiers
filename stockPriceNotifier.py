from time import sleep, time
from matplotlib.pyplot import title
from nsetools import Nse
import pyttsx3
from plyer import notification

engines=pyttsx3.init('sapi5')


rate =engines.getProperty('rate')
voices =engines.getProperty('voices')

engines.setProperty('rate',150)
engines.setProperty('voices',voices[0].id)

def speak(audio):
    engines.say(audio)
    engines.runAndWait()


nse=Nse()
while True:
    tatamotors=nse.get_quote('tatamotors')

    print(f"The current price of TataMotors is :- {tatamotors['buyPrice1']}")

    tittle="Price Alert for Tata Motors"
    message=f"The current price of Tata motors is {tatamotors['buyPrice1']}"
    notification.notify(title=tittle,message=message)
    speak(message)

    if tatamotors['buyPrice1']>=415.00:
        tittle="Price Alert for Tata Motors"
        message="The current price of Tata motors is above 415.You can sell your stock"
        notification.notify(title=tittle,message=message)
        speak(message)
        
    if tatamotors['buyPrice1']<=405.00:
        tittle="Price Alert for Tata Motors"
        message="The current price of Tata motors is below 405.Its best time to buy stock."
        notification.notify(title=tittle,message=message)
        speak(message)
