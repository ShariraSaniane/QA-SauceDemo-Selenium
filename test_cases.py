import pytest  

@pytest.mark.run(order=1)
def test01_login():
    pass

@pytest.mark.run(order=2)
def test02_sorting():
    pass

@pytest.mark.run(order=3)
def test03_cart():
    pass

@pytest.mark.run(order=4)
def test04_your_cart():
    pass

@pytest.mark.run(order=5)
def test05_checkout():
    pass
