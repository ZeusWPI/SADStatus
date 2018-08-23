import urllib.request


def is_online(url):
    try:
        return urllib.request.urlopen(url).getcode() == 200
    except Exception:
        return False
