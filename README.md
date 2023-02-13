# 📜 WhatsApp chat to JSON

This Python script converts an exported WhatsApp chat .txt file to a JSON file. 
This repository also contains a sample chat .txt file and a generated JSON file for reference.
Feel free to dabble around with them if you'd like.

The script assumes that the exported chat file content (datetime, "-" and ":" separators) is as follows:

```` (Example)
30.7.2016 22.47 - Linus: Hello there!
30.7.2016 22.48 - Bill: General Kenobi!
31.7.2016 14.38 - Jeff: I am your father!
31.7.2016 14.38 - Elon: That's impossible!
31.7.2016 14.39 - Anton: What's the most you ever lost on a coin toss?
````
If so, then you're good to go!

Open your preferred CLI and navigate to a directory of your choosing, and then

```` (Example)
git clone https://github.com/zachvengenz/whatsapp-chat-to-json.git
cd whatsapp-chat-to-json
````
1. Copy your chat.txt file here
2. Open whatsapp.py
3. Change line 5 to match your chat .txt file name
4. Change line 24 to what you want the JSON file to be called
5. Save changes
6. Run the script from your CLI:

```` (Example)
python whatsapp.py
````
Or just simply run it from your editor.

If everything went according to plan, the result should look something like this:

```JSON
[
    {
        "date": "30.7.2016",
        "time": "22.47",
        "sender": "Linus",
        "message": "Hello there!"
    },
    {
        "date": "30.7.2016",
        "time": "22.48",
        "sender": "Bill",
        "message": "General Kenobi!"
    },
    {
        "date": "31.7.2016",
        "time": "14.38",
        "sender": "Jeff",
        "message": "I am your father!"
    },
    {
        "date": "31.7.2016",
        "time": "14.38",
        "sender": "Elon",
        "message": "That's impossible!"
    },
    {
        "date": "31.7.2016",
        "time": "14.39",
        "sender": "Anton",
        "message": "What's the most you ever lost on a coin toss?"
    }
]
```
