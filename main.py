import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
NAME = os.getenv("NAME")
URL = "https://api.github.com/users/" + NAME


def main():
    response = requests.get(URL, headers={"Authorization": TOKEN,
                                          "Accept": "application/vnd.github+json",
                                          "X-GitHub-Api-Version": "2022-11-28"})
    info = response.json()
    to_save = {"Name": "name",
               "Company": "company",
               "Bio": "bio",
               "Location": "location",
               "Email": "email",
               "Twitter": "twitter_username",
               "Public repositories": "public_repos",
               "Public gists": "public_gists",
               "Followers": "followers",
               "Following": "following",
               "Created at": "created_at",
               "Updated at": "updated_at",
               "Login": "login",
               "Link": "html_url"}
    with open('info.txt', 'w') as f:
        for i in to_save:
            if info[to_save[i]] is not None:
                f.write(f"{i}: {info[to_save[i]]}\n")


if __name__ == "__main__":
    main()
