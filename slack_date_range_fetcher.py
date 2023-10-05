from dotenv import load_dotenv
import os
import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import argparse
from datetime import datetime

# Load .env file
load_dotenv()

user_cache = {}  # Initialize user cache

def fetch_messages_from_slack_channel(client, channel_id, start_date, end_date):
    try:
        response = client.conversations_history(
            channel=channel_id,
            oldest=start_date.timestamp(),
            latest=end_date.timestamp()
        )

        messages = response['messages']
        for message in messages:
            user_id = message.get('user')
            if user_id:
                if user_id not in user_cache:  # If not cached, fetch and cache
                    user_info = client.users_info(user=user_id)
                    user_cache[user_id] = {
                        'id': user_info['user']['id'],
                        'name': user_info['user']['name'],
                        'real_name': user_info['user']['real_name'],
                        'display_name': user_info['user']['profile']['display_name']
                    }

                message['user_info'] = user_cache[user_id]  # Retrieve from cache
                
        return messages
    except SlackApiError as e:
        print(f"Slack API Error: {e.response['error']}")
        return []

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch Slack messages within a date range from a specific channel')
    parser.add_argument('channel_id', type=str, help='Slack Channel ID')
    parser.add_argument('start_date', type=lambda d: datetime.strptime(d, '%Y-%m-%d'), help='Start date in YYYY-MM-DD format')
    parser.add_argument('end_date', type=lambda d: datetime.strptime(d, '%Y-%m-%d'), help='End date in YYYY-MM-DD format')
    
    args = parser.parse_args()
    bot_token = os.getenv("BOT_TOKEN")
    client = WebClient(token=bot_token)

    messages = fetch_messages_from_slack_channel(client, args.channel_id, args.start_date, args.end_date)
    print(json.dumps(messages, indent=4, ensure_ascii=False))
