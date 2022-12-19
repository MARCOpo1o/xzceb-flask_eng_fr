'''
This file contains the code for the translator
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

autenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=autenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    '''this translates english to french'''
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return french_text

def french_to_english(french_text):
    """this translates french to english"""
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return english_text
