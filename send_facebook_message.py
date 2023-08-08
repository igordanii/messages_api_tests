import vonage

application_id = "e16fd307-eb15-4c92-ab9e-8159e7026386"

client = vonage.Client(application_id=application_id,private_key=open("./private.key").read().strip())

response =client.messages.send_message(
  {
   "message_type": "text",
   "text": "Daniel testanto. Confime se recebeu",
   "to": "1335893171",
   "from": "112808445238772",
   "channel": "messenger"
}
)

print(response)