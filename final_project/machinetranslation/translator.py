
'''
This Module uses IBM_WatSON language translator service
to translate the user provided text
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(englishtext):
    '''
    Method translats the user provided english text into french
    '''
    try:
        translation = language_translator.translate(
        text=englishtext,
        model_id='en-fr').get_result()
        translation_value=translation["translations"][0]["translation"]
    except Exception as inst:
        abc= str(inst).split(",")[1]
        return abc
    return translation_value

def french_to_english(frenchtext):
    '''
    Method translats the user provided frewnch text into english
    '''
    try:
        translation = language_translator.translate(
        text=frenchtext,
        model_id='fr-en').get_result()
        translation_value=translation["translations"][0]["translation"]
    except Exception as inst:
        abc= str(inst).split(",")[1]
        return abc
    return translation_value

