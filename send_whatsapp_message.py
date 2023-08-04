import vonage

application_id = "e16fd307-eb15-4c92-ab9e-8159e7026386"

client = vonage.Client(application_id=application_id,private_key=open("./private.key").read().strip())

client.messages.send_message(
    {
        "channel":"whatsapp",
        "message_type":"text",
        "text":"Só estou tentando a API de WhatsApp",
        "from":"18483014573",
        "to":"558888736070"
    }
)
