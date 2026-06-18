import httpx

from core.base import Module


class DiscordTokenModule(Module):
    name = "discordtoken"
    description = "Gets information from a valid discord token."

    def run(self, token: str) -> dict:
        resp = httpx.get(
            "https://discord.com/api/v9/users/@me",
            headers = {"authorization": token}
        )

        if resp.status_code != 200:
            return {"error": resp.text}
        
        return {"result": resp.json()}