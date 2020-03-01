from flask import Flask,render_template,request
import requests
import json
from random import randint
app=Flask(__name__)
global mob_num
global name
li=[]


@app.route('/')
def home():
    return render_template('otp.html')


@app.route('/generate',methods=['POST'])
def generate():
    #URL = 'https://www.sms4india.com/api/v1/sendCampaign'
    name1=request.form['n']
    mob_num=request.form['n1']
    otp=""
    for i in range(0,4):
        otp+=str(randint(0,9))
    li.clear()
    li.append(otp)
    print(otp)
    """def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
      req_params = {
      'apikey':apiKey,
      'secret':secretKey,
      'usetype':useType,
      'phone': phoneNo,
      'message':textMessage,
      'senderid':senderId
      }
      return requests.post(reqUrl, req_params)
    otp_body="Hello" + name1 + "Your OTP is :" + otp
    response = sendPostRequest(URL, 'E3SVUDP9E8I6IGXP7ZD5VOOKM3XM5DZX', 'OMZHBIN93TTWV4IU', 'stage',mob_num, 'srdharanidharan2000@gmail.com',otp_body)
    print(response.text)"""
    return render_template("validate.html")


@app.route('/validate',methods=['POST'])
def validate():
    va=request.form['vat']
    
    #print(li)

    if str(li[0])==str(va):
        ct="OTP Validation Successfull!!!"
        return render_template("result1.html",c=ct)
    else:
        ct="OTP Validation Failed!!!"
        return render_template("result.html",c=ct)
    #li=[]
    


if __name__=="__main__":
    app.run(debug=True)
