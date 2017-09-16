import os
from tradingAPI import *

brow = os.getenv('DRIVER')
api = API("CRITICAL")


def test_launch():
    assert api.launch(brow)


def test_login():
    assert api.login("james.lumper@gmail.com", "TestTest1.")


def test_movs():
    api.addMov("usd/euro", 1)
    api.checkPos()
    stock = [x.id for x in api.movements if x.name ==
             "usd/euro" and x.quantity == 1][0]
    api.closeMov(stock)
    api.checkPos()
    assert len([x.id for x in api.movements if x.name ==
                "ethereum" and x.quantity == 1][0]) == 0


def test_clearPrefs():
    assert api.clearPrefs()


def test_addPrefs():
    assert api.addPrefs(["bitcoin", "ethereum"])


def test_logout():
    assert api.logout()
