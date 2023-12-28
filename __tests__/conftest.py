# conftest.py
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="local",
                     help="Specify the environment (local, dev, prod)")
