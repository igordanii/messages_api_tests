import vonage

class Vonage_Client:
    
    def __init__(self):
        self.application_id = "e16fd307-eb15-4c92-ab9e-8159e7026386"
        self.client = vonage.Client(application_id=self.application_id,private_key=open("./private.key").read().strip())

    def get_client(self):
        print(open("./private.key").read().strip())
        return self.client