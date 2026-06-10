import httpx

from core.base import BaseModule


class IpLookupModule(BaseModule):
    name = "iplookup"
    description = "Gets information from an IP address."

    def run(self, ip_addr: str):
        resp = httpx.get(f"https://iplocate.io/api/lookup/{ip_addr}")

        if resp.status_code != 200:
            return {"error": resp.text}
        
        data = resp.json()
        company = data.get("company")
        privacy = data.get("privacy")

        return {
            "result": {
                "country": data.get("country"),
                "state": data.get("state"),
                "city": data.get("city"),
                "provider": company.get("name"),
                "VPN?": privacy.get("is_vpn"),
                "proxy?": privacy.get("is_proxy")
            }
        }
