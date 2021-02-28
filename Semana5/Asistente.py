import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "e7625830-7962-11eb-a677-955fddca88ea3629bd31-9ffe-44c8-a3e2-a1c374f2a7c3"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


while True:
    pregunta = input("Escribe tu pregunta: ")
    demo = classify(pregunta)

    label = demo["class_name"]
    confidence = demo["confidence"]


    if label == "Informacion":
        print("Te envio toda la información")
        print ("result: '%s' with %d%% confidence" % (label, confidence))
    elif label == "Playa":
        print("Playa")
        print ("result: '%s' with %d%% confidence" % (label, confidence))
        