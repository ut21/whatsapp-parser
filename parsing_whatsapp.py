import re
import datetime
import pandas

class Message:
    
    time : datetime.datetime
    author : str
    content : str
    
    def __init__(self, time, author, content):
        self.time = time
        self.author = author
        self.content = content

pattern = re.compile(r'(\d{2}/\d{2}/\d{2}), (\d{1,2}:\d{2} [ap]m) - ([^:]+): (.*)')

def read_messages(filename):
    with open(filename, 'r', encoding='utf-8', newline='') as f:
        lines = f.readlines()
    lines = lines[1:]
    parsed_messages = []
    for line in lines:
        line = line.strip()
        line = line.replace('\u202f', ' ')


        match = pattern.match(line)
        if match:
            date = match.group(1)
            time = match.group(2)
            author = match.group(3)
            content = match.group(4)
            time = datetime.datetime.strptime(f'{date} {time}', '%d/%m/%y %I:%M %p')
            message = Message(time, author, content)
            parsed_messages.append(message)
        
        else:
            parsed_messages[-1].content += '\n' + line
    
    df = pandas.DataFrame([vars(m) for m in parsed_messages])
    return df

df= read_messages('chat.txt')
print(df.head())
    


