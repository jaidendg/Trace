import httpx

from core.base import Module, Result


class DiscordTokenModule(Module):
    name = "discordtoken"
    description = "Gets information from a valid discord token."

    def run(self, token: str):
        resp = httpx.get(
            "https://discord.com/api/v9/users/@me",
            headers = {"authorization": token}
        )

        if resp.status_code != 200:
            return Result(error=resp.text)
        
        return Result(data=resp.json())