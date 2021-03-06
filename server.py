import sentry_sdk

from bottle import Bottle, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    "https://eb331728cfe24029aab9c16a40f20af0@o524862.ingest.sentry.io/5638035",
    traces_sample_rate=1.0
)

app = Bottle()

@route("/success/")
def hello_world():
    return "Hello World!" 

@route("/fail/")
def error(param):
    raise RuntimeError

def fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@route("/fib/<n:int>")
def fib_handler(n):
    result = fib(n)
    return str(result)

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
