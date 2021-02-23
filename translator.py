#Paul Burgess
#Imports

from ibm_watson import LanguageTranslatorV3

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#Used for testing
#import json
#from pandas import json_normalize
#-

#URL and keys
#Language Translator
URL_LT = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/f9dd2f2b-cfde-49c6-a6cc-7740f755020a'
APIKEY_LT = '17QbHlyM2DApzjBv_Nv43RzDO4kZdSKP6CO5EQxaikpj'
VERSION_LT = '2018-05-01'
#-

#Authentication
    #Language Translator
authenticator = IAMAuthenticator(APIKEY_LT)
language_translator = LanguageTranslatorV3(version=VERSION_LT, authenticator=authenticator)
language_translator.set_service_url(URL_LT)
#-
#Step 3
def englishtofrench(text_en):
    if (isinstance(text_en, str) and text_en != ""):
        text_fr = language_translator.translate(text=text_en, model_id='en-fr').get_result()
        text_fr = text_fr['translations'][0]['translation']
        return text_fr
    return None
#Step 5
def englishtogerman(text_en):
    if (isinstance(text_en, str) and text_en != ""):
        text_de = language_translator.translate(text=text_en, model_id='en-de').get_result()
        text_de = text_de['translations'][0]['translation']
        return text_de
    return None
