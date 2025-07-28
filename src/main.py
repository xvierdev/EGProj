from flask import Flask, render_template
import modules.func_test


app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'base.html',
        content=modules.func_test.func_test()
    )


if __name__ == "__main__":
    app.run(debug=True)
