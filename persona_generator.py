import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_persona(posts, comments):
    data_blob = ""

    for i, post in enumerate(posts):
        data_blob += f"\nPost {i+1}: {post['title']}\n{post['selftext']}\n"

    for i, comment in enumerate(comments):
        data_blob += f"\nComment {i+1}: {comment['body']}\n"

    prompt = f"""
Based on the Reddit activity below, generate a full User Persona describing interests, personality traits, values, tone, and opinions. 
Cite each post or comment number like (Post 2) or (Comment 4).

{data_blob}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
