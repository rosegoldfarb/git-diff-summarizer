import argparse
import subprocess
from openai import OpenAI
from dotenv import load_dotenv
import requests


def get_git_diff(pr_url):
    diff_url = pr_url + ".diff"
    response = requests.get(diff_url)
    return response.text

def summarize_text (text):
    client = OpenAI()

    messages = [ {"role": "system", "content": "You are a code reviewer that provides a concise and simple summary of the changes made in a pull request. List the changes in bullet form and group the bullets by the file the changes take place in."}]
    messages.append({"role": "user", "content": text})

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    return completion.choices[0].message.content

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Summarize Git diff file using OpenAI API.")
    parser.add_argument("pr_url", type=str, help="Link to the PR URL.")
    args = parser.parse_args()
    pr_diff = get_git_diff(pr_url=args.pr_url)
    summary = summarize_text( pr_diff)

    print("PR Summary:")
    print(summary)

if __name__ == "__main__":
    main()
