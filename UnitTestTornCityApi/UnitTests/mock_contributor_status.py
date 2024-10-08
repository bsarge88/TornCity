import pandas

import torn_requester


def mock_contributor_stats(self, stat) -> pandas.DataFrame:
    selection = "contributors"
    request = f"https://api.torn.com/{self.object}/{self.faction_id}?selections={selection}"
    request += f"&stat={stat}"
    results = self.requester.request(request)
    stats = results["contributors"][stat]  # ContrbuterStat(stat, results)
    df = pandas.DataFrame.from_dict(stats, 'index')
    df = df[df['in_faction'] == 1]
    return df.rename(columns={"contributed": stat, "in_faction": f"{stat}_in_faction"})
