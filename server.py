from bottle import route
from bottle import run

# регистрируем обработчик пути /hello/ с помощью декоратора route
@route("/hello/")
def hello_world():
    return "Hello World!"  # Возвращаем приветственное сообщение

@route("/upper/<param>")
def upper(param):
    return param.upper()

def fib(n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
    return a

@route("/fib/<n:int>")
def fib_handler(n):
    result = fib(n)
    return str(result)

if __name__ == "__main__":
    # Запускаем веб-сервер с помощью функции run: указываем адрес узла и порт
    run(host="localhost", port=8080, debug=True)
    # Булев флаг debug=True запускает сервер в режиме отладки