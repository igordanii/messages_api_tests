import vonage
client = vonage.Client(key="ada6657d", secret="FGMchK1u0YXeBVGW")

print(client.messages.send_message({
    "channel":"sms",
    "message_type":"text",
    "from":"5588988128333",
    "to":"5588988433024",
    "text":"Vamos ficar ricos?",
}))

