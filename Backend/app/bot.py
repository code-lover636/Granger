from bardapi import Bard
import bardapi
import os


def response(input_text):
    try:
        # set your __Secure-1PSID value to key
        os.environ['_BARD_API_KEY']="WQjrFrYyflUWRKRDNgZoooPdxjBrB7Dx4gD0mzqsJMW55NK_GSNYfUIngm31zQjnFW_jBA."
        bard = Bard(timeout=10)
        # Send an API request and get a response.
        response = bardapi.core.Bard().get_answer(input_text)
        print(response)
        return response['content']
    except:
        return "Sorry I am unable to respond to that query"