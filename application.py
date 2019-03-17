from flask import Flask, render_template, request, url_for
import json
import pygal

app = Flask(__name__)

@app.route("/")
def index():
    with open("test.json", "r") as read_file:
        data = json.load(read_file)
        # img = io.BytesIO()
        # plt.plot(data["heartBeats"])
        # plt.savefig(img, format='png')
        #     # return data["heartBeats"]
        # img.seek(0)
        # plot_url = base64.b64encode(img.getvalue()).decode()
        graph = pygal.Line()
        graph.title = '% Change Coolness of programming languages over time.'
        x_axies = []
        print(len(data["heartBeats"]))
        for index, hb in enumerate(range(len(data["heartBeats"]))): 
            #print(hb)
            x_axies.append(index)
        #print("/n")
        #print(x_axies)
        graph.x_labels = x_axies
        graph.add('test',data["heartBeats"])
        graph_data = graph.render_data_uri()
        return render_template("index.html", graph_data = graph_data)
    

@app.route("/usrScreen")
def usrScreen():
    with open("test.json", "r") as read_file:
        data = json.load(read_file)
    return render_template("usrScreen.html", heartBeats = data["heartBeats"][-1])

if __name__ == '__main__':
    app.run(debug=True)

