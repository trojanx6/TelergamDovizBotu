import telebot 
import requests as req 
from bs4 import BeautifulSoup as btu
token = "5704829126:AAHRwvozF5m0UD4PmyLe2tEUz8qI-9542Yc"
bot = telebot.TeleBot(token)
url = "https://bigpara.hurriyet.com.tr/doviz/"
istek = req.get(url)
html = istek.text
soup = btu(html, "html.parser")
tbody = soup.find("div",{"class":"tBody"})
lis = []
for i  in tbody:
    pr = i.text
    lis.append(pr)
    
    
dolar = lis[1]
euro = lis[3]
ingliz = lis[5]
isvicre = lis[7]
japon = lis[9]
sudi = lis[11]
norvec = lis[13]
danimarka = lis[15]
avus =  lis[17]
kanada = lis[19]
isciv = lis[21]
rublee = lis[23]
    
@bot.message_handler(commands=["dolar"]) # telergam botundaki emirler /dolar dedigimiz zaman
def do(message): #  içindeki degere bir veri gelecek
    global dolar
    bot.send_message(message.chat.id, dolar) # bu ise yanitladi olarak degil mesaj gonderir 
    
    
@bot.message_handler(commands=["euro"])
def eu(message):
    global euro
    bot.send_message(message.chat.id, euro)
    
    

@bot.message_handler(commands=["ingilizStrelini"])
def ing(message):
    global ingliz
    bot.send_message(message.chat.id, ingliz)
    
    
    
@bot.message_handler(commands=["isvicreKronu"])
def isv(message):
    global isvicre 
    bot.send_message(message.chat.id,isvicre )
    
    
    
@bot.message_handler(commands=["japonyeni"])
def jp(message):
    global japon
    bot.send_message(message.chat.id, japon)    
    
    

@bot.message_handler(commands=["suudiArabistan"])
def ssd(message):
    global sudi
    bot.send_message(message.chat.id, sudi)

    
@bot.message_handler(commands=["norveckronu"])
def nor(message):
    global norvec
    bot.send_message(message.chat.id, norvec)       
    
    
            
@bot.message_handler(commands=["danimarkakronu"])
def da(message):
    global danimarka
    bot.send_message(message.chat.id,danimarka )              
    
        
                    
                        
@bot.message_handler(commands=["avusturlyadolari"])
def aos(message):
    global aus
    bot.send_message(message.chat.id, aus)             
    
                                  
                                
                                    
                                        
@bot.message_handler(commands=["kanadadolar"])
def kan(message):
    global kanada
    bot.send_message(message.chat.id, kanada)
    
    
                                                                                                     
@bot.message_handler(commands=["isveckronu"])
def start(message):
    global isciv 
    bot.send_message(message.chat.id, isciv)         
    
                            

@bot.message_handler(commands=["rusyaruble"])
def start(message):
    global rublee
    bot.send_message(message.chat.id, rublee)



@bot.message_handler(commands=["help"])
def start(message):
    msh = """
 /help  --> 
    /dolar
    /euro
    /ingilizStrelini
    /isvicreKronu
    /japonyeni
    /suudiArabistan
    /norveckronu
    /danimarkakronu
    /avusturlyadolari
    /kanadadolar
    /isveckronu
    /rusyaruble
    Github:https://github.com/trojanx6
    Kullandiginiz icin tesskur ederim :)
    
    """
    bot.send_message(message.chat.id, msh)
    
    
 
def main():
    bot.polling()
    
if __name__=="__main__":
    main()