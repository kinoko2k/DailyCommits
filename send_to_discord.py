import requests
import json
import os
import sys

def send_discord_message(commit_count):
    webhook_url = os.environ['DISCORD_WEBHOOK']
    
    data = {
        'embeds': [
            {
                'title': 'コミットかうんたー (1day)',
                'description': f'今日のこみっと数：{commit_count}',
                'color': 16711680
            }
        ]
    }
    
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        print(f"Discordへのメッセージの送信に失敗しました。Status code: {response.status_code}")
        sys.exit(1)

if __name__ == "__main__":
    commit_count = sys.argv[1]
    send_discord_message(commit_count)
