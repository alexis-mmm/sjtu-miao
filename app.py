from flask import Flask, request, jsonify
from mysql import *
from get_jpg import *
from run_detection import *


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/result', methods=['POST'])
def giveresult():
    if request.method == 'POST':
        rxjson = request.get_json()
        id = rxjson['id']
        print(id)
        id, name, sex, color, habit, picture = getById(id)
        data = {}
        data["id"] = id
        data["name"] = name
        data["sex"] = sex
        data["color"] = color
        data["habit"] = habit
        data["picture"] = picture
        return jsonify(data)


@app.route('/match', methods=['POST'])
def matchcat():
    if request.method == 'POST':
        rxjson = request.get_json()
        # url = request.form['imgUrl']
        url = rxjson['imgUrl']
        print(url)
        cat = []
        res = {}

        fetch_test_picture(URL=url)
        ranks = run_detection()
        for i, rank in enumerate(ranks):
            id, name, sex, color, habit, picture = getById(rank)
            res[i] = {}
            res[i]["id"] = id
            res[i]["name"] = name
            res[i]["sex"] = sex
            res[i]["color"] = color
            res[i]["habit"] = habit
            res[i]["picture"] = picture
            cat.append(res[i])
            if i >= 1:
                break

        return jsonify(res)


@app.route('/forum/get', methods=['GET'])
def getLatestInfo():
    if request.method == 'GET':
        results = refreshForum()
        info = []
        res = {}
        for i, result in enumerate(results):
            res[i] = {}
            res[i]["id"] = result[0]
            res[i]["usrid"] = result[1]
            res[i]["title"] = result[2]
            res[i]["content"] = result[3]
            res[i]["avatar"] = result[4]
            res[i]["img"] = result[5]
            res[i]["time"] = result[6]
            res[i]["likes"] = result[7]
            info.append(res[i])
        return jsonify(info)


@app.route('/forum/load', methods=['GET'])
def loadInfo():
    if request.method == 'GET':
        end = request.args.get('key')
        print(end)
        results = loadForumInfo(end)
        info = []
        res = {}
        for i, result in enumerate(results):
            res[i] = {}
            res[i]["id"] = result[0]
            res[i]["usrid"] = result[1]
            res[i]["title"] = result[2]
            res[i]["content"] = result[3]
            res[i]["avatar"] = result[4]
            res[i]["img"] = result[5]
            res[i]["time"] = result[6]
            res[i]["likes"] = result[7]
            info.append(res[i])
        return jsonify(info)


@app.route('/forum/post', methods=['POST'])
def insertforum():
    if request.method == 'POST':
        rxjson = request.get_json()
        usrid = rxjson['id']
        title = rxjson['title']
        content = rxjson['content']
        avatar = rxjson['avatar']
        image = rxjson['image']
        time = rxjson['time']
        likes = 0
        insertInForum(usrid, title, content, avatar, image, time, likes)
        results = refreshForum()
        info = []
        res = {}
        for i, result in enumerate(results):
            res[i] = {}
            res[i]["id"] = result[0]
            res[i]["usrid"] = result[1]
            res[i]["title"] = result[2]
            res[i]["content"] = result[3]
            res[i]["avatar"] = result[4]
            res[i]["img"] = result[5]
            res[i]["likes"] = result[6]
            res[i]["time"] = result[7]
            info.append(res[i])
        return jsonify(info)


@app.route('/insert', methods=['GET', 'POST'])
def insertcat():
    if request.method == 'POST':
        color = request.form['color']
        des = request.form['des']
        insert(color, des)
        data = {}
        data["color"] = color
        data["des"] = des
        return jsonify(data)


if __name__ == '__main__':
    app.run(
        debug=True
    )



