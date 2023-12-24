import argparse
import subprocess
import openai


def get_git_diff(file_path):
    command = f"git diff {file_path}"
    result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
    return result.stdout

def summarize_text(api_key, text):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=100,
        temperature=0.5,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

def main():
    parser = argparse.ArgumentParser(description="Summarize Git diff file using OpenAI API.")
    parser.add_argument("file_path", type=str, help="Path to the Git diff file.")
    parser.add_argument("api_key", type=str, help="Your OpenAI API key.")
    args = parser.parse_args()

    git_diff = get_git_diff(args.file_path)
    summary = summarize_text(args.api_key, git_diff)

    print("Git Diff Summary:")
    print(summary)

if __name__ == "__main__":
    main()
