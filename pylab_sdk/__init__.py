import os

import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import random
import string
import platform


_PYLAB_API_ENDPOINT = "https://api.pylab.co"
_PYLAB_AUTH_KEY = os.environ.get("PYLAB_AUTH_KEY", "")


def auth(key: str) -> None:
    global _PYLAB_AUTH_KEY
    _PYLAB_AUTH_KEY = key


def get_ip() -> str:
    """Get public ip from http header"""
    s = requests.Session()
    retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
    s.mount("http://", HTTPAdapter(max_retries=retries))
    s.mount("https://", HTTPAdapter(max_retries=retries))
    try:
        response = s.get(f"{_PYLAB_API_ENDPOINT}/ip")
    except requests.exceptions.RequestException:
        return ""

    if response.status_code != 200:
        return ""

    return response.text


def get_latest_agents(arch=None) -> str | dict | None:
    """Get latest user agent of modern browser"""
    s = requests.Session()
    retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
    s.mount("http://", HTTPAdapter(max_retries=retries))
    s.mount("https://", HTTPAdapter(max_retries=retries))
    try:
        response = s.get(f"{_PYLAB_API_ENDPOINT}/agents")
    except requests.exceptions.RequestException:
        return

    if response.status_code != 200:
        return

    data = response.json()
    if arch:
        if arch in data:
            return data[arch]
        else:
            raise KeyError
    else:
        return data


CONTENT_TYPE_TEXT = "00"
CONTENT_TYPE_CODE = "01"
CONTENT_TYPE_IMAGE = "02"
CONTENT_TYPE_FILE = "03"


def wc(content: str, content_type: str = CONTENT_TYPE_TEXT, source: str = "") -> bool:
    """Webcat"""
    try:
        response = requests.post(
            f"{_PYLAB_API_ENDPOINT}/wc",
            data={"content": content, "content_type": content_type, "source": source},
            headers={"Authorization": f"Bearer {_PYLAB_AUTH_KEY}"},
        )
    except requests.exceptions.RequestException:
        return False

    if response.status_code != 200:
        return False

    return True


webcat = wc


def random_alphanumeric(length) -> str:
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))


def say(text="") -> None:
    """Text to Speech, platform independently"""
    sanitized_text = text.strip().replace("'", "").replace('"', "")

    system = platform.system()
    if system == "Darwin":
        os.system(f'say "{sanitized_text}"')
    elif system == "Linux":
        os.system(f'spd-say "{sanitized_text}"')
    elif system == "Windows":
        os.system(
            '''"PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{}');"'''.format(
                sanitized_text
            )
        )
    else:
        raise NotImplementedError
