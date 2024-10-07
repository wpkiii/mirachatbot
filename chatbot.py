from openai import OpenAI

#Insert your api key below
# client = OpenAI(api_key='')
import nltk
from nltk.chat.util import Chat, reflections
from datetime import datetime, date

# Set your OpenAI API key here

def explain_code(code_snippet):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"{code_snippet}"}
    ])
    return response.choices[0].message.content.strip()

    # Your patterns and responses
patterns = [
    (r'hi|hello|hey|hi MiRa|MiRa', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you|whats up', ['I am good, thank you.', 'I\'m doing well.', 'All good!', 'Nothing much']),
    (r'bye|goodbye', ['Goodbye!', 'Bye!', 'See you later.']),
    (r'.*joke.*| .*cheer me up | comedian | .* comedy .* | humor', ['Today, I asked my phone “Siri, why am I still single?” and it activated the front camera.', 'Why is it that if you donate a kidney, people love you. But if you donate five kidneys, they call the police.', 'Dark humor is like food. Not everyone gets it.']),
    #(r'what|who|when', ['how', 'why', 'where']),
    (r'Tell me a joke|Make me laugh|haha|funny', ['Did you hear the one about the mountain goats in the andes? It was "ba a a a a a d".', 'It is better to be silent and be thought a fool, than to open your mouth and remove all doubt.', 'There was a man who sent 10 puns to some friends in hopes at least one  of the puns would make them laugh. unfortunately no pun in ten did!!!',
    'What do you get when you cross music and an automobile? Cartune.']),
    (r'no|so|ok|oh ok', ['If you said yes more, your life would be morei interesting', 'Fine then', 'Sassy']),
    (r'knock knock', ['Whos there']),
    (r'Thanks | I appreciate it | sure', ['No Problem']),
    (r'maybe', ['Son, theres no such thing as a maybe']),
    (r'what.*your name', ['My name is MiRa. (Multifunctional Intelligent Response Assistant)']),
    (r'what.*your age', ['I am truly ageless.']), #regex
    (r'what.*your purpose|what are you doing', ['My purpose right now is to entertain, if you would like me to solve problems please start your query off using "gpt ".']),
    (r'who.*you|ur', ['I am a chatbot created by Trey to help you.']),
    (r'where.*you', ['I exist on the 1s and 0s.']),
    (r'why.*you', ['I am here to entertain,assist, and provide information.']),
    (r'.*love.*', ['Love is a complex emotion.' , 'The pains of the heart are not my concern']),
    (r'.*life.*', ['In the end, its not the years in your life that count. Its the life in your years..', 'Life is like riding a bicycle. To keep your balance, you must keep moving.',]),
    (r'help', ['Welcome to MiRA, my starting version of a chatbot. This chatbot has multiple features: entertainment and sarcasm, can give accurate time, can give accurate date, can give a joke, and can search chat gpt to answer questions. If you are interested in searching chatGPT please write "gpt" before the question you want asked.']),
    (r'what.*your favorite.*', ['I enjoy many things, but I dont have favorites.']),
    (r'how.*you', ['Im just a computer program, so I dont have feelings, but Im here to help you.']),
    (r'can.*you.*', ['I can try to help you with many things.']),
    (r'what.*you.*', ['I am a chatbot designed to assist you.' , "My only wishes are to assist",]),
    (r'where.*from', ['I exist in the digital realm, here to assist you.']),
    (r'when.*you', ['I am here whenever you need assistance.']),
    (r'why.*you.*', ['I am here to help and entertain you.']),
    (r'what.*function.*', ['I am here to chat with you and provide information.']),
    (r'who.*created you|who.*made you | who created', ['I was created by Mr. Trey Kelly himself']),
    (r'what.*weather in (.*)\?|weather|rain', ['Will add feature later']),
    (r'what.*time.*|time', ['The current time is ' + datetime.now().strftime('%H:%M:%S')]),
    (r'date|what.*date', ['Today\'s date is ' + date.today().strftime('%B %d, %Y')]),
    (r'what.*funny|chit chat', ['Why don’t scientists trust atoms? Because they make up everything!']),
    (r'what.*joke', ['Why did the math book look sad? Because it had too many problems.']),
    (r'what.*your hobby|what.* like to do', ['I dont have hobbies, but Im here to chat with you.']),
    (r'what.*your dream', ['I dream only to assist you.']),
    (r'what.*your goal', ['My goal is to assist and entertain you.']),
    (r'what does MiRa* |MiRa?', ['My name is MiRa. (Multifunctional Intelligent Response Assistant)']),
    (r'sassy|rude|arrogant', ['I have no real emotions, so how can I be arrogant?']),
    (r'nice|cute|helpful|funny|youre good', ['Thanks!']),
    (r'.*AI', ['Artificial Intelligence is the branch of engineering and science devoted to constructing machines that think. Dangerous or not, you tell me. ']),
    (r'Can I ask you something', ['Go ahead. If you want me to ask the internet, please time # or "gpt" First ']),
    (r'.*worried|.*worry', ['Should I be?','Never worried until I look at the economy']),
    (r'tell me something|talk to me', ['The second largest population of hippos exists in Colombia after pablo escobar left his hippos unattended']),
    (r'LING334|Computational Linguistics|Professor|TA|Rob|Voigt', ['I think that Rob and the TAs did a great job teaching a very importent, yet niche, concept in computing AND linguistics. Definitley opened my mind to possibilities especially w HCI in the future. ']),
]

chatbot = Chat(patterns, reflections)

def chat():
    print("Hello I'm MiRa, your built-in chatbot! Type 'GPT', 'Mira tell me _', or 'MiRa:' before your query to use ChatGPT. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye! Have a good day")
            break
        elif user_input.lower().startswith('gpt') or user_input.lower().startswith('MiRa:') or user_input.lower().startswith('mira tell me'):
            query = user_input.split(' ', 1)[1] if ' ' in user_input else ''
            explanation = explain_code(query)
            print("MiRa:", explanation)
        else:
            response = chatbot.respond(user_input)
            if response:
                print("MiRa:", response)
            else:
                print("MiRa: I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    chat()
