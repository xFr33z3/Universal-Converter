import webview
from threading import Thread, Event
from app import app
import temp

stop_event = Event()

app_title = "File Converter"
host = 'http://127.0.0.1'
port = 5000
def run():
    while not stop_event.is_set():
        app.run(debug=True, use_reloader=False)

if __name__ == "__main__":
    f = Thread(target=run)
    f.daemon = True
    f.start()

    window = webview.create_window(
        app_title,
        f"{host}:{port}",
        width=1020,
        height=720
    )

    webview.start()
    
    stop_event.set()

    