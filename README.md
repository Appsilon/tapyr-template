# PyShiny Dashboard Template

## How to run

### Devcontainer

The best way is to use the predefined [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers).
This way just run:

```sh
poetry shell
shiny run app.py --reload
```

### Poetry

This template uses `poetry` for packages management.
The best way to install `poetry` is with `pipx`.

### Deployment on Posit Connect 

First set your `CONNECT_API_KEY` as environmental variable.
Then add your server.
And finally deploy.

```sh
CONNECT_API_KEY="AppsilonAppsilonAppsilonAppsilon"

rsconnect add \
--api-key $CONNECT_API_KEY \
--server <MY_CONNECT_URL> \
--name <SERVER_NAME>

rsconnect deploy shiny -t "PyShiny Template" .
```