import requests


def get_ip():
    """Get public ip from http header"""
    response = requests.get('https://pylab.co/ip')
    if response.status_code != 200:
        raise RuntimeError()
    return response.text


def get_latest_agents(arch=None):
    """Get latest user agent of modern browser"""
    response = requests.get('https://pylab.co/agents')
    if response.status_code != 200:
        raise RuntimeError()
    data = response.json()
    if arch:
        if arch in data:
            return data[arch]
        else:
            raise KeyError
    else:
        return data


def wc(content, source=''):
    response = requests.post('https://pylab.co/wc', data={
        'token': '47853878',
        'content': content,
        'source': source
    })
    if response.status_code != 200:
        raise RuntimeError
    return
