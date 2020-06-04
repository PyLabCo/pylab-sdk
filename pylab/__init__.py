import requests


def get_ip():
    """Get public ip from http header"""
    try:
        response = requests.get('https://pylab.co/ip', max_retries=5)
    except requests.exceptions.RequestException:
        return ''

    if response.status_code != 200:
        return ''

    return response.text


def get_latest_agents(arch=None):
    """Get latest user agent of modern browser"""
    try:
        response = requests.get('https://pylab.co/agents', max_retries=5)
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


def wc(content, source=''):
    try:
        response = requests.post('https://pylab.co/wc', data={
            'token': '47853878',
            'content': content,
            'source': source
        })
    except requests.exceptions.RequestException:
        return False

    if response.status_code != 200:
        return False

    return True
