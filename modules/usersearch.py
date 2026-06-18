import httpx
import json
from core.base import Module


class UserSearchModule(Module):
    name = "usersearch"
    description = "Searches username for social media accounts."

    async def request(self, client: httpx.AsyncClient, url: str) -> bool:
        try:
            resp = await client.get(url)
            return resp.status_code < 400
        except:
            return False

    async def run(self, username: str):
        with open("configs/user_search.json") as f:
            socials = json.load(f)

        valid = {}

        async with httpx.AsyncClient() as client:
            for social, data in socials.items():
                api_url = data["api"] + username

                if await self.request(client, api_url):
                    valid[social] = data["default"] + username

        return {"result": valid}