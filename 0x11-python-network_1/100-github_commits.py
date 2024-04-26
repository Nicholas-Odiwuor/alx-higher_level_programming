import requests
import sys

def list_commits(repository, owner):
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: Failed to fetch commits. Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repository> <owner>")
        sys.exit(1)
    repository = sys.argv[1]
    owner = sys.argv[2]
    list_commits(repository, owner)

