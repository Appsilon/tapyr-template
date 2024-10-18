from shiny.pytest import create_app_fixture

# https://shiny.posit.co/py/docs/end-to-end-testing.html
# This has a hidden @pytest.fixture inside and is picked up by all tests in the current directory
app = create_app_fixture("../../app.py")
