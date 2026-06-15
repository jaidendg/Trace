import httpx

from core.base import BaseModule


class GithubModule(BaseModule):
    name = "github"
    description = "Finds email from github user."
    arguments = ["username"]

    def run(self, username: str) -> dict:
        resp = httpx.get(f"https://api.github.com/users/{username}/repos")
        if resp.status_code != 200:
            return {"error": resp.text}

        username_lower = username.lower()
        emails = []

        for repo in resp.json():
            commits_url = repo["commits_url"][:-6]

            r = httpx.get(commits_url)
            if not (200 <= r.status_code < 400):
                continue

            commits = r.json()
            if not commits:
                continue

            commit = commits[0]
            author = commit["author"]

            if author.get("login", "").lower() != username_lower:
                continue

            emails.append(commit["commit"]["author"]["email"])

        return {"result": emails}