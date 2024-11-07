import json
import logging

import aiohttp
import asyncio

log = logging.getLogger(__name__)

class AmadeusClient:
    def __init__(self, token: str, base_url: str = 'https://api.travelpayouts.com'):
        self.__token = token
        self.base_url = base_url
        self._auth_url="https://test.api.amadeus.com/v1/security/oauth2/token"
        self._client_id = 'rIFYAdJnDDHb8ZZCg7BruAXDtRhAjD3H'
        self._client_secret = 'uDLYx7pECWvkIpAx'
    async def get_token(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"grant_type": "client_credentials",
                "client_id": self._client_id,
                "client_secret": self._client_secret}



        async with aiohttp.ClientSession() as session:
            async with session.get(self._auth_url,data=data,headers=headers) as resp:
                access_token = await resp.json()
                access_token = access_token["access_token"]
                return access_token


    async def get_best_hotels(self):
        access_token = await  self.get_token()
        headers = {'Authorization': 'Bearer' + ' ' + access_token}
        hotel_lists_url = 'https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city'
        hotel_lists_params = {
            "cityCode": "BDH",
            "radius": 100,
            "radiusUnit": "KM",
            "hotelSource": "ALL"
        }
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(hotel_lists_url,
                                       params=hotel_lists_params,
                                       headers=headers) as resp:
                    hotels = await resp.json()
                    return hotels
            except aiohttp.ClientError as e:
                log.error(e)
