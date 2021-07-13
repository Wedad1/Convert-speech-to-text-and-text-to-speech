from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
apikey = 'XDAvW3OdtkKLgGLDDQERRGEysBlX0zxIBPESHNsrfXTq'
url = 'https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/50163564-7bb2-4036-9a2a-7021494670a8'


def main():


    authenticator = IAMAuthenticator(apikey)
    TtS = TextToSpeechV1(authenticator=authenticator)
    TtS.set_service_url(url)
    with open('text.txt', 'r') as file: 
        text = file.read()

    with open('speech.mp3', 'wb') as audio_file:
        res = TtS.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
        audio_file.write(res.content)

if __name__ == "__main__":
    main()
   