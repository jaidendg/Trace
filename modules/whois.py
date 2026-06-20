import whois

from core.base import Module, Result


class WhoisModule(Module):
    name = "whois"
    description = "Domain WHOIS information lookup."

    def run(self, domain: str):
        try:
            data = whois.whois(domain)

            return Result(data = {
                    "domain": domain,
                    "registrar": data.registrar,
                    "creation date": str(data.creation_date),
                    "expiration date": str(data.expiration_date),
                    "name servers": data.name_servers
                })

        except Exception as e:
            return Result(error=e)