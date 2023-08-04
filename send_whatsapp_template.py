import vonage

application_id = "4783f4a8-98fd-48b7-8cf2-2d80a01b7e86"

client = vonage.Client(application_id=application_id,private_key=open("./private.key").read().strip())

client.messages.send_message({
   "message_type": "template",
   "template": {
      "name": "2e989322_84ae_436d_bcd6_9bcbe0639d25:reach_out",
      "parameters": ["2526"]},
   "to": "558888736070",
   "from": "18483014573",
   "channel": "whatsapp",
   "whatsapp": {
      "policy": "deterministic",
      "locale": "pt_BR"
   }
})

