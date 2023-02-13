import re
import json

# change 'chat_file_name.txt' to match your chat file
with open('chat_file_name.txt', 'r', encoding='utf-8') as f:
    chat_history = f.read()

chat_list = []
for line in chat_history.strip().split('\n'):
    match = re.match(r'(\d{1,2}\.\d{1,2}\.\d{4} \d{1,2}\.\d{2}) - ([^:]+): (.*)', line)
    if match:
        datetime_str, sender, message = match.groups()
        date, time = datetime_str.split(' ')
        chat_list.append({
            'date': date,
            'time': time,
            'sender': sender,
            'message': message
        })
    else:
        chat_list[-1]['message'] += '\n' + line.strip()

# change 'chat_file_name.json' to what you want the file to be called
with open('chat_file_name.json', 'w', encoding='utf-8') as f:
    json.dump(chat_list, f, ensure_ascii=False, indent=4)
