This is a simple Python utility for getting an up-to-date list of free proxies from [clarketm/proxy-list](https://github.com/clarketm/proxy-list). It reads the list from their Github repo, and returns a list of dicts in the following format:
```python
{
    "ip": "76.80.19.107",
    "port": "8080",
    "protocol_guess": "http"
}
```

Just copy-paste the `get_proxies` function into your project.