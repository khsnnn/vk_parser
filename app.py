import requests
import json
import argparse
import os


ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
API_URL = os.getenv('API_URL', 'https://api.vk.com/method/')

def get_user_info(user_id):
    url = f'{API_URL}users.get?user_ids={user_id}&access_token={ACCESS_TOKEN}&v=5.131'
    response = requests.get(url)
    return response.json()

def get_followers(user_id):
    url = f'{API_URL}users.getFollowers?user_id={user_id}&access_token={ACCESS_TOKEN}&v=5.131&extended=1&fields=screen_name'
    response = requests.get(url)
    return response.json()

def get_subscriptions(user_id):
    url = f'{API_URL}users.getSubscriptions?user_id={user_id}&access_token={ACCESS_TOKEN}&v=5.131&extended=1&fields=screen_name'
    response = requests.get(url)
    return response.json()

def get_groups(user_id):
    url = f'{API_URL}groups.get?user_id={user_id}&access_token={ACCESS_TOKEN}&v=5.131&extended=1&fields=screen_name'
    response = requests.get(url)
    return response.json()


def save_to_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main(user_id, output_file):
    user_info = get_user_info(user_id)
    followers = get_followers(user_id)
    subscriptions = get_subscriptions(user_id)
    groups = get_groups(user_id)

    data = {
        'user_info': user_info,
        'followers': followers,
        'subscriptions': subscriptions,
        'groups': groups
    }

    save_to_json(data, output_file)
    print(f"Информация сохранена в файл: {output_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='VK API User Info')
    parser.add_argument('--user_id', type=int, default=274881868, help='ID пользователя ВК')
    parser.add_argument('--output_file', type=str, default='vk_user_info.json', help='Путь к файлу для сохранения результата')

    args = parser.parse_args()

    main(args.user_id, args.output_file)
