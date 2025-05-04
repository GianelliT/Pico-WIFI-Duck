import socketpool
import wifi
from duck import exe
import os
from adafruit_httpserver import Server, Request, JSONResponse ,POST , Response
"""--------------------------------------------------------------------------------------"""
ssid = "Pico WIFI DUCK"
password = "pico123456"
"""--------------------------------------------------------------------------------------"""
print("Creating access point", ssid)
wifi.radio.stop_station()
wifi.radio.start_ap(ssid, password)
print("Access point created!")
pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)
"""--------------------------------------------------------------------------------------"""
@server.route("/")
def base(request: Request):
    with open("index.html", "r") as file:
        html_content = file.read()
    headers = {"Content-Type": "text/html"}
    return Response(request, html_content, headers=headers)
"""--------------------------------------------------------------------------------------"""
@server.route("/api", POST,append_slash=True)
def api(request: Request):
    if request.method == POST :
        req = request.json()
        payload = req["content"]
        payload = payload.splitlines()
        exe(payload)
        return JSONResponse(request, {"message": "Done"})
"""--------------------------------------------------------------------------------------"""
@server.route("/list_payloads", append_slash=True)
def list_payloads(request: Request):
    files = [f for f in os.listdir("payloads") if f.endswith(".txt") and not f.startswith(".")]
    return JSONResponse(request, {"files": files})
"""--------------------------------------------------------------------------------------"""
@server.route("/load_payload", POST, append_slash=True)
def load_payload(request: Request):
    data = request.json()
    filename = data.get("filename")
    try:
        filepath = f"payloads/{filename}"
        with open(filepath, "r") as f:
            content = f.read()
        return JSONResponse(request, {"content": content})
    except Exception as e:
        return JSONResponse(request, {"error": str(e)}, status=500)
"""--------------------------------------------------------------------------------------"""
@server.route("/save_payload", POST)
def save_payload(request: Request):
    try:
        req = request.json()
        filename = req.get("filename", "").strip()
        content = req.get("content", "").strip()
        if not filename:
            return JSONResponse(request, {"error": "Missing filename"}, status=400)
        if not "payloads" in os.listdir():
            os.mkdir("payloads")
        if ".." in filename or "/" in filename:
            return JSONResponse(request, {"error": "Invalid filename"}, status=400)
        path = f"payloads/{filename}"
        with open(path, "w") as f:
            f.write(content)
        return JSONResponse(request, {"message": "Saved successfully!"})
    except Exception as e:
        return JSONResponse(request, {"error": str(e)}, status=500)
"""--------------------------------------------------------------------------------------"""
server.serve_forever('192.168.4.1', 80)
