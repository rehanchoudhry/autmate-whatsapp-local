from wa_automate_socket_client import  SocketClient


client = SocketClient("https://rehan-171.herokuapp.com/",'171')


def repy(message):
    data = message["data"]
    text = data["text"]
    number = data["from"]
    #client.sendText(number, "Good Day")
    if text == "sareha":
        client.sendText(number, "Laddu")
    if text == "haram":
        client.sendText(number, "Barfi")
    if text == "arham":
        client.sendText(number, "Sohn Halwa")
    if text == "saveil":
        client.sendText(number, "Gulaab Jaman")
    if text == "naveil":
        client.sendText(number, "Russ Gula")
client.onMessage(repy)
