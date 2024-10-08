import pandas
import requests


def _check_errors(results):
    # {"error":{"code":2,"error":"Incorrect key"}}
    if "error" in results:
        raise Exception(f'API call failed with {results["error"]}')


class TornRequester:
    def __init__(self, torn_key: str):
        self.torn_key={"key": torn_key}

    def request(self, object, id, selection, field="")  -> pandas.DataFrame:
        request = f"https://api.torn.com/{object}/{id}"
        params = {"selections": f"{selection}{field}"} | self.torn_key
        try:
            results = requests.get(request, params=params).json()
        except requests.exceptions.HTTPError as errh:
            raise RuntimeError(f"HTTP Error calling Torn API") from errh
        # request = f"https://api.torn.com/{object}/{id}?selections={selection}{field}"
        # results = requests.request(url=request, method="get")
        _check_errors(results)
        return pandas.DataFrame.from_dict(results, 'index')

