import webview
class Api():
    def log(self):
        print("value")


window = webview.create_window(
    "localhost",
    url='localhost:3000',
    js_api=Api(),
)
webview.start()
