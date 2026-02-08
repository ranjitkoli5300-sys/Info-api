from flask import Flask, request, Response
import requests

app = Flask(__name__)

CALLAPP_URL = "https://s.callapp.com/callapp-server/csrch"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Linux; Android 12; ONEPLUS A6013 Build/SQ3A.220705.004; wv) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 "
        "Chrome/108.0.5359.128 Mobile Safari/537.36"
    ),
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

@app.route("/info", methods=["GET"])
def info():
    num = request.args.get("name")
    if not num:
        return Response("Missing num parameter", status=400)

    params = {
        "cpn": f"+{num}",
        "myp": "gp.118069622193383141492",
        "ibs": "0",
        "cid": "0",
        "tk": "0007729042",
        "cvc": "2236"
    }

    r = requests.get(CALLAPP_URL, headers=HEADERS, params=params, timeout=15)

    return Response(
        r.content,
        status=r.status_code,
        content_type=r.headers.get("Content-Type", "application/json")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
