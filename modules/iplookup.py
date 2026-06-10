import httpx

from core.base import BaseModule


class IpLookup(BaseModule):
    name = "iplookup"
    description = "Gets information from an IP address."

    def run(self, ip_addr: str):
        resp = httpx.get(f"https://iplocate.io/api/lookup/{ip_addr}")
        if resp.status_code != 200:
            return {"error": resp.text}
        
        rj = resp.json()
        result = {
            "country": rj["country"],
            "State": rj["subdivision"],
            "city": rj["city"],
            "provider": rj["company"]["name"],
            "VPN?": rj["privacy"]["is_vpn"],
            "proxy?": rj["privacy"]["is_proxy"]
        }

        return {"result": result}
