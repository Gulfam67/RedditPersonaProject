import sys
from urllib.parse import urlparse
from scrape_user import scrape_reddit_user
from persona_generator import generate_persona
from write_persona import save_to_file

def extract_username(url):
    return urlparse(url).path.strip("/").split("/")[-1]

if __name__ == "__main__":
    url = input("Paste the Reddit profile URL: ")
    username = extract_username(url)
    posts, comments = scrape_reddit_user(username)
    persona = generate_persona(posts, comments)
    save_to_file(username, persona)
    print(f"User Persona saved as {username}_persona.txt!")
