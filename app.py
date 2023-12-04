import os
import requests
from dotenv import load_dotenv
from slack_bolt import App

load_dotenv()


app = App(
  token = os.environ.get("SLACK_BOT_TOKEN"),
  signing_secret = os.environ.get("SLACK_SIGNING_SECRET")
)

def get_random_joke():
  response = requests.get(
    f"https://v2.jokeapi.dev/joke/any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single",
    headers={
      "Accept": "application/json"
    }
  )
  
  joke = response.json().get("joke")
  return joke

@app.command("/joke")
def joke_command(ack, say, command):
  ack()
  joke = get_random_joke()
  say(joke)

if __name__ == "__main__":
  app.start(port=int(os.environ.get("PORT", 3000)))