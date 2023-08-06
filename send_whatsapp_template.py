import vonage

application_id = "e16fd307-eb15-4c92-ab9e-8159e7026386"

client = vonage.Client(application_id=application_id,private_key=open("./private.key").read().strip())

response = client.messages.send_message({
   "message_type": "template",
   "template": {
      "name": "2e989322_84ae_436d_bcd6_9bcbe0639d25:reach_out",
      "parameters": ["2526"]},
   "to": "558888128333",
   "from": "18483014573",
   "channel": "whatsapp",
   "whatsapp": {
      "policy": "deterministic",
      "locale": "pt_BR"
   }
})

print(response)

