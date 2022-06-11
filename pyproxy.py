from typing import List

import requests as requests


def get_proxies() -> List[dict]:
    raw_proxy_list = requests.get(
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt").text
    refined_proxy_list = []
    for proxy_line in raw_proxy_list.splitlines():
        ip, port = proxy_line.split(":")
        protocol_guess = "https" if port == "443" else "http"
        refined_proxy_list.append({"ip": ip, "port": port, "protocol_guess": protocol_guess})
    return refined_proxy_list


if __name__ == "__main__":
    print(get_proxies())
