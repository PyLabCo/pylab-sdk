def test_get_ip():
    import pylab
    assert len(pylab.get_ip().split('.')) == 4


def test_get_latest_agents():
    import pylab
    assert 'macOS' in pylab.get_latest_agents()


def test_wc():
    import pylab
    assert pylab.wc('hello', source='test') is None
    assert pylab.wc('world') is None
