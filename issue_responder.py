import os
import google.generativeai as genai
import requests

def post_comment(repo, issue_number, comment):
    """Posts a comment to a GitHub issue."""
    url = f"https://api.github.com/repos/{repo}/issues/{issue_number}/comments"
    headers = {
        "Authorization": f"token {os.environ['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {"body": comment}
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()

def main():
    """The main function."""
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    # Determine the prompt based on what triggered the workflow
    if "COMMENT_BODY" in os.environ and os.environ["COMMENT_BODY"]:
        prompt = os.environ["COMMENT_BODY"]
    else:
        prompt = os.environ["ISSUE_BODY"]

    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    response = model.generate_content(prompt)

    post_comment(
        os.environ["REPO_FULL_NAME"],
        os.environ["ISSUE_NUMBER"],
        response.text,
    )

if __name__ == "__main__":
    main()
