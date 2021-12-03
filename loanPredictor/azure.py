import urllib.request
import json
import os
import ssl

def userInput(g1, m1, d1, e1, s1, a1, c1, h1, p1, l1):

    def allowSelfSignedHttps(allowed):
        # bypass the server certificate verification on client side
        if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
            ssl._create_default_https_context = ssl._create_unverified_context

    allowSelfSignedHttps(True)  # this line is needed if you use self-signed certificate in your scoring service.

    a1 = int(a1) / 72
    a1 = format(max(0, round(a1)))
    a1 = str(a1)
    c1 = int(c1) / 72
    c1 = format(max(0, round(c1)))
    c1 = str(c1)
    g, m, d, e, s, a, c, h, p, l = g1, m1, d1, e1, s1, a1, c1, h1, p1, l1
    # Request data goes here
    data = {
        "data":
        [
            {
                'Gender': g,
                'Married': m,
                'Dependents': d,
                'Education': e,
                'Self_Employed': s,
                'ApplicantIncome': a,
                'CoapplicantIncome': c,
                'Credit_History': h,
                'Property_Area': p,
                'Loan_Amount_Term': l,
            },
        ],
    }

    body = str.encode(json.dumps(data))

    url = 'Your Azure Url'
    api_key = 'Your API Key' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = json.loads(response.read())
        arr = result.split('[')
        r=arr[1]
        arr = r.split(']')
        r=arr[0]
        arr = r.split('.')
        r = arr[0]
        r=int(r)*72
        r=format(max(0, round(r)))
        result=str(r)
        print(result)
        return result
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))
        return 0
