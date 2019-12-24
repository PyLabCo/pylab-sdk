# pylab-sdk
A development kit that collects simple utilities.

## Installation

```bash
pip install pylab-sdk
```

## Example
```
import pylab


# Get your public IP
ip = pylab.get_ip()

# Get latest user agent of modern browser
agents = pylab.get_latest_agents()
assert agents['macOS'] == pylab.get_latest_agents('macOS')

# Similar to netcat, webcat running over the http protocol helps you keep a log that you can check anywhere.
pylab.wc('hello world', source='discord-bot')

```
