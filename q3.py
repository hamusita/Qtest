import requests
import sys 
import json

key = sys.argv.pop(1)

judge = {
    "paper":{
        "paper": "引き分け！",
        "rock": "あなたの勝ち！",
        "scissors":"あなたの負け！"
    },
    "rock":{
        "paper": "あなたの負け！",
        "rock": "引き分け！",
        "scissors":"あなたの勝ち！"
    },
    "scissors":{
        "paper": "あなたの勝ち！",
        "rock": "あなたの負け！",
        "scissors":"引き分け！" 
    }
}

r = requests.get('https://nh-a811fa16.herokuapp.com/').text
r = list(json.loads(r).values())[0]

result = judge[key][r]

print("you(" + key + ") / me(" + r + ") : " + result)