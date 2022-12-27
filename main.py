from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def currency_calc(in_cur, to_cur):
  curr_url = f"https://www.x-rates.com/calculator/?from={in_cur}&to={to_cur}&amount=1"
  response = requests.get(curr_url)
  page= response.text
  soup= BeautifulSoup(page,'html.parser')
  rate =  soup.find('span', class_='ccOutputRslt').get_text()
  return rate
  

@app.route('/')
def home():
  return '<h1>Currency Rate API </h1> <p>Sample URL: /api/v1/inr--usd </p>'

@app.route('/api/v1/<input_curr>--<out_curr>/')
def get_curr_rate(input_curr,out_curr):
  rate = currency_calc(input_curr,out_curr)
  return f"Input Currency = {input_curr.upper()} " \
         f"Output Currency = {out_curr.upper()} " \
         f"Currency Rate = {rate}"


app.run(host='0.0.0.0' , debug= True)
