import requests
import datetime
import os

# ユーザー名を設定する
username = 'your_username'

# 今日の日付と昨日の日付を取得する
today = datetime.date.today().isoformat()
yesterday = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()

# GitHub REST APIのエンドポイントURLを構築する
url = f'https://api.github.com/users/{username}/events'

# アクセストークンをシークレットから取得する
access_token = os.environ['ACCESS_TOKEN']

# APIリクエストを送信する
headers = {'Authorization': f'token {access_token}'}
response = requests.get(url, headers=headers)

# レスポンスから今日と昨日のコミット数を取得する
events = response.json()
today_commit_count = sum(1 for event in events if event['type'] == 'PushEvent' and event['created_at'].startswith(today))
yesterday_commit_count = sum(1 for event in events if event['type'] == 'PushEvent' and event['created_at'].startswith(yesterday))

# Discord Webhookに送信する準備
webhook_url = os.environ['DISCORD_WEBHOOK']
data = {
    "embeds": [
        {
            "title": "今日のこみっと",
            "description": f"今日のこみっと数：{commit_count}\n昨日のこみっと数：{yesterday_commit_count}",
            "color": 16711680  # 赤色
        }
    ]
}

# Discord WebhookにPOSTリクエストを送信
response = requests.post(webhook_url, json=data)

# レスポンスのステータスコードをチェック
if response.status_code == 204:
    print('コミット数が、Discordに正常に送信されました！')
else:
    print(f'コミット数を、Discordに送信できませんでした。Status code: {response.status_code}')
