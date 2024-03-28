from flask import Flask, request, Response, stream_with_context
import random
import time
# from openai import AzureOpenAI

app = Flask(__name__)

answers = [
    "Certainly, yes!",
    "I don't think so.",
    "It's very likely.",
    "Probably not.",
    "Let me check on that.",
    "Could you ask again later?"
]

def generate_answer(question):
    print(f"Received question: {question}")
    # Simulate processing delay
    
    selected_answer = random.choice(answers)
    print(f"Answer: {selected_answer}")
    for word in selected_answer.split():
        yield f"{word} "
        time.sleep(0.5)  # Simulate a delay between words for streaming effect
        
    for i in range(10):
        yield f"{i} "
        time.sleep(0.5) 

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question', '')
    # return Response(generate_answer(question), content_type='text/plain') #'application/json')   
    return app.response_class(stream_with_context(generate_answer(question)))
