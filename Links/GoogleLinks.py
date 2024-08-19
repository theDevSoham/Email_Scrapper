from enum import Enum

class GoogleLinks(Enum):
    BASE_URL = "https://www.google.com/search?q=+"
    POSITION = "hr"
    LOCATION = "Bangalore"
    DOMAIN = "@gmail.com"

    @classmethod
    def get_url(cls, data):
        return f'{cls.BASE_URL.value}"{data["position"].replace(" ", "+") or cls.POSITION.value}" "{data["location"].replace(" ", "+") or cls.LOCATION.value}" "{data["domain"] or cls.DOMAIN.value}" -intitle:"profiles" -inurl:"dir/ " site:in.linkedin.com/'