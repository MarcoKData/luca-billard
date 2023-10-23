from project import app, render_template, jsonify, request
import webbrowser
import threading
import json


PATH_TO_TXT_FILES = "./txt_files"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/write_to_files", methods=["POST"])
def write():
    request_post = request.json
    for filename, content in request_post.items():
        player_param = True
        if "_1" in filename:
            player_number = 1
        elif "_2" in filename:
            player_number = 2
        else:
            player_param = False
        
        if player_param:
            path = f"{PATH_TO_TXT_FILES}/player_{player_number}/{filename}.txt"
        else:
            path = f"{PATH_TO_TXT_FILES}/{filename}.txt"

        with open(path, "w") as file:
            file.write(content)

    return jsonify({"status": "ok"})


def start_app():
    app.run(debug=False)


def open_webbrowser():
    webbrowser.open("http://127.0.0.1:5000")


if __name__ == "__main__":
    """x1 = threading.Thread(target=start_app)
    x1.start()

    x2 = threading.Thread(target=open_webbrowser)
    x2.start()"""
    app.run(debug=True)
