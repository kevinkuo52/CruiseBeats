from flask import Flask, render_template, request
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
        graph.x_labels = ['1','2','3','4','5','6']
        graph.add('test',data["heartBeats"])
        graph_data = graph.render_data_uri() 
        return render_template("index.html", graph_data = graph_data)
    

@app.route("/func")
def func():
    return '<h1>testo1</h1>'

if __name__ == '__main__':
    app.run(debug=True)

