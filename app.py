from flask import Flask
import os
import socket
import json
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route("/")
def hello():
    htmlTree = None
    with open('template/data.json', 'rb') as dataFile:
        userData = json.load(dataFile)
        print(userData)
        htmlTree = ET.ElementTree()
        htmlTree.parse('template/template.html')
        for k,v in userData.items():
            e = list(htmlTree.iter(k))[0]
            e.text = v
    ET.dump(htmlTree)
    html = ET.tostring(htmlTree.getroot(), method='html')
    return html

def main():
    app.run(host='0.0.0.0', port=os.getenv('PORT', 8000))

if __name__ == "__main__":
    main()
