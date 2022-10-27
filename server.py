from flask import Flask, send_from_directory
import logging
import os
import requests
import json

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
    
@app.route("/")
def root():
  return send_from_directory('.', 'bootstrap.html')

@app.route("/data.json")
def newroute():
  BACKEND_URL = "https://" + str(os.getenv('BACKEND_URL')) + "/getdata"
  logging.info("Getting backend data from " + str(BACKEND_URL))
  leaderboard_data = requests.get(BACKEND_URL)
  logging.debug(leaderboard_data.json())
  
  return str(leaderboard_data.json()).replace("\'", "\"")

if __name__ == "__main__":
  app.run(port=5002)

