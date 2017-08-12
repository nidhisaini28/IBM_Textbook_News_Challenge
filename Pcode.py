from flask import Flask, render_template,request
import pandas as pd
import numpy as np
from os.path import join, dirname 
import httplib, urllib, base64
import json
import discovery
import NLUpython
import sys  
import markupsafe
reload(sys)  
sys.setdefaultencoding('utf8')

app = Flask(__name__, static_url_path = "", static_folder = "tmp")

@app.route('/')
def index():


	return render_template('main.html')
  	

@app.route('/test', methods=['POST'])
def test():
    if request.method=='POST':
        print "I am here.."
        text = request.form['newsSearch'];
        print "text: ", text
        headers = {'Content-Type': 'application/json','Ocp-Apim-Subscription-Key': 'd3d6a1dd9dfe46fab1b4ce7620850dc1'}
        params = urllib.urlencode({}) 
        body={"question":str(text), "top": 1}
        try:
            conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
            conn.request("POST", "/qnamaker/v2.0/knowledgebases/3b38c629-ab42-4d17-baa3-03b9aeb29b0f/generateAnswer?%s" % params, str(body), headers)
            response = conn.getresponse()
            
            data = response.read()
            results = json.loads(data)
            print results
            conn.close()
        except Exception as e:
            print e
        outputlist = []
        keyword_main = NLUpython.NLUData(text)
        useful_link = discovery.discoveryData(keyword_main[0])
        print results
        outputlist.append(text)
        outputlist.append(results["answers"][0]["answer"])
        outputlist.append(useful_link[0])
        outputlist.append(useful_link[1])
        
    return render_template('test.html',output=outputlist)    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5601,debug=True)