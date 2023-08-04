import vonage

client = vonage.Client(key="ada6657d",secret="FGMchK1u0YXeBVGW")

print(client.messages.send_message({
    "channel":"sms",
    "message_type":"text",
    "from":"Vonage",
    "to":"5588988736070",
    "text":"Vamos ficar ricos?",
}))
