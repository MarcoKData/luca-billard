from project import app, render_template, jsonify, request


PATH_TO_TXT_FILES = "/Users/marcokleimaier/Documents/SoftwareentwicklungKleimaier/projekte/luca-billard/txt_files"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/write_to_files", methods=["POST"])
def write():
    request_post = request.json
    for filename, content in request_post.items():
        print(filename, content)
        
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


if __name__ == "__main__":
    app.run(debug=True)
