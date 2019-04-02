from flask import Flask, Response, request
import os
import socket
import json
import xml.etree.ElementTree as ET
import markdown2
import pdfkit

app = Flask(__name__)

@app.route("/", methods=['POST'])
def pdf():
    userData = request.get_json()
    htmlTree = None
    htmlTree = ET.ElementTree()
    htmlTree.parse('static/template.html')
    for k,v in userData.items():
        e = list(htmlTree.iter(k))[0]
        content = '<SectionContent>' + markdown2.markdown(v) + '</SectionContent>'
        node = ET.fromstring(content)
        e.append(node)
    html = ET.tostring(htmlTree.getroot(), method='html')

    css = 'static/template.css'
    pdf = pdfkit.from_string(html.decode('utf-8'), False, css=css)

    res = Response(pdf)
    res.mimetype = 'application/pdf'
    return res

def main():
    app.run(host='0.0.0.0', port=os.getenv('PORT', 8000))

if __name__ == "__main__":
    main()
