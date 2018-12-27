from sanic import Sanic, response

app = Sanic()


@app.route("/", methods=frozenset(('POST', )))
async def index(request):
    return response.json({"Hello,": "world!"})


def start():
    app.run(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    start()
