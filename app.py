from flask import Flask, render_template
from flask_restful import Api
from MetroData import FirstAndLast, latest_news
from MetroData import TripDuration
from MetroData import TripFrequencies

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return render_template('index.html')


api.add_resource(FirstAndLast.FirstLast, '/firstlast')
api.add_resource(TripDuration.TripDuration, '/duration')
api.add_resource(TripFrequencies.TripFrequencies, '/frequency')
api.add_resource(latest_news.News, '/news')

if __name__ == "__main__":
    app.run()
