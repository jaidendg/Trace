import httpx

from core.base import Module, Result


class IpLookupModule(Module):
    name = "iplookup"
    description = "Gets information from an IP address."

    def run(self, ip_address: str):
        resp = httpx.get(f"https://iplocate.io/api/lookup/{ip_address}")

        if resp.status_code != 200:
            return Result(error=resp.text)
        
        data = resp.json()
        company = data.get("company")
        privacy = data.get("privacy")

        return Result(data = {
                "country": data.get("country"),
                "state": data.get("state"),
                "city": data.get("city"),
                "provider": company.get("name"),
                "VPN?": privacy.get("is_vpn"),
                "proxy?": privacy.get("is_proxy")
            })
