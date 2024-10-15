from shiny.pytest import create_app_fixture

# https://shiny.posit.co/py/docs/end-to-end-testing.html
app = create_app_fixture("../../app.py")
