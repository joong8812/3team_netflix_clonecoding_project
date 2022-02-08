import requests, json


# binary -> kakao stt api -> text
def kakaoSttRequest(binary):
    URL = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
    API_KEY = "6381239402cbea39806f6263757a66ea" # kakao rest api key

    headers = {
        "Content-Type": "application/octet-stream",
        # "Transfer-Encoding": "chunked",
        "Authorization": "KakaoAK "+ API_KEY,
    }


    # with open('heykakao.wav', 'rb') as fp:
    #     b = fp.read()


    # with open('mp3.mp3', 'wb') as f:
    #     f.write(binary)

    with open('mp3_1.wav', 'rb') as f:
        b = f.read()

    res = requests.post(URL, headers=headers, data=b)

    print(res.text)

    return res.text


def naverCSRRequest(binary):
    URL = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=Kor"
    API_KEY_ID = "hdghf4cmxw"
    API_KEY = "pDk4cmJW7gQnPoA6yNIIojCpFxV8STnxtW7opeQv"

    headers = {
        "Content-Type": "application/octet-stream",
        "X-NCP-APIGW-API-KEY-ID": API_KEY_ID,
        "X-NCP-APIGW-API-KEY": API_KEY
    }





    res = requests.post(URL, headers=headers, data=binary)

    print(res.text)

    return json.loads(res.text)