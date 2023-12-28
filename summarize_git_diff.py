import argparse
import subprocess
from openai import OpenAI
from dotenv import load_dotenv


def get_git_diff(file_path):
    command = f"git diff {file_path}"
    result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
    return result.stdout

def summarize_text (text):
    client = OpenAI()

    messages = [ {"role": "system", "content": "You are a code reviewer that provides a concise and simple summary of the changes found in a Git diff file. Provide the summary in bullet format."}]
    changes = text.split('\n\n')

    for change in changes:
        messages.append({"role": "user", "content": change})

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    return completion.choices[0].message.content

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Summarize Git diff file using OpenAI API.")
    parser.add_argument("file_path", type=str, help="Path to the Git diff file.")
    args = parser.parse_args()

    git_diff = get_git_diff(args.file_path)
    summary = summarize_text( git_diff)

    print("Git Diff Summary:")
    print(summary)

if __name__ == "__main__":
    main()
