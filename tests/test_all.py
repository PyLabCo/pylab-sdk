def test_get_ip():
    import pylab_sdk as pylab

    assert len(pylab.get_ip().split(".")) == 4


def test_get_latest_agents():
    import pylab_sdk as pylab

    assert "macOS" in pylab.get_latest_agents()


def test_wc():
    import pylab_sdk as pylab

    assert pylab.wc("hello", source="test") is None
    assert pylab.wc("world") is None
