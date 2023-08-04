import vonage

application_id = "e16fd307-eb15-4c92-ab9e-8159e7026386"

client = vonage.Client(application_id=application_id,private_key=open("./private.key").read().strip())

client.messages.send_message(
   {
   "message_type": "image",
   "image": {
      "url": "https://www.sabornamesa.com.br/media/k2/items/cache/8097da6161421504ad99a7e5f09e9e69_XL.jpg",
      "caption": "Encomende já este bolo"
   },
   "to": "558893171183",
   "from": "18483014573",
   "channel": "whatsapp"
}
)
