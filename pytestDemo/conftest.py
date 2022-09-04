import pytest


@pytest.fixture(scope="class")
# @pytest.fixture()
def setup():
    print("I will be executing first ")
    yield
    print("I will executed last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Gulnawaz", "Arshad", "gulnawazarshadacademy.com"]


# @pytest.fixture(params=["Chrome", "Firefox", "IE"])
@pytest.fixture(params=[("Chrome", "Gulnawaz", "Arshad"), ("Firefox", "Dilnawaz"), ("IE", "Fatima")])
def crossBrowser(request):
    return request.param

