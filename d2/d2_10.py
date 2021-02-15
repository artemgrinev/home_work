import sentry_sdk

from bottle import Bottle, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    "https://eb331728cfe24029aab9c16a40f20af0@o524862.ingest.sentry.io/5638035",
    traces_sample_rate=1.0
)

app = Bottle()

@app.route("/success/")
def hello_world():
    return "Hello World!" 

@app.route("/fail/")
def index():  
    raise RuntimeError("There is an error!")  
    return
    
def fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@app.route("/fib/<n:int>")
def fib_handler(n):
    result = fib(n)
    return str(result)

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
