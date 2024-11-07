import aiohttp
import logging

log = logging.getLogger(__name__)


class AviasalesClient:
    def __init__(self, token: str, base_url: str = 'https://api.travelpayouts.com'):
        self.__token = token
        self.base_url = base_url

    def _build_url(self, path: str):
        return f"{self.base_url}/{path}"

    async def get_latest_prices(
            self,
            origin_city: str,
            destination_city: str,
            month: str,
            trip_duration: str,
    ):
        """
        Return the cheapest price for each dayes
        month in format YYYY-MM-DD or YYYY-MM
        https://travelpayouts.github.io/slate/?shell#the-calendar-of-prices-for-a-month
        """
        api_path = self._build_url("v2/prices/month-matrix")
        headers = {
            "x-access-token": self.__token,
        }

        params = {
            "origin": origin_city,
            "destination": destination_city,
            "month": month,
            "currency": "rub",
            "show_to_affiliates": "false",
        }

        log.info("Get request for path %s, with params: %r", api_path, params)
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(api_path, headers=headers, params=params) as resp:
                    return await resp.json()
            except aiohttp.ClientError as e:
                log.error(e)
