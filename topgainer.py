from nsetools import Nse
from flask import Flask
import pprint

app = Flask(__name__)

gainers={}

nse = Nse()
companies=nse.get_top_gainers()


@app.route('/today')
def gainer():
    for item in companies:
        gainers[item['symbol']]=item['netPrice']
    
    pprint.pprint(gainers)
    return gainers

if __name__ == '__main__': 
    app.run()
