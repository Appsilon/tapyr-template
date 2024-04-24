# Tapyr - Shiny for Python Application Template<a href="https://appsilon.github.io/tapyr-template/"><img src="www/images/tapyr.png" align="right" alt="Tapyr logo" style="height: 140px;"></a>

> Create and deploy PyShiny dashboards with ease.

# WIP: Not the final version of README.

## Introduction

Tapyr is designed for data scientists and developers seeking a seamless transition from development to deployment, this template uses `poetry` for dependency management and `pytest`/`playwright` for comprehensive app validation/testing/quality assurance.
Ideal for projects aiming for high-quality code and efficient deployment on Posit Connect.

## Docs

For comprehensive documentation, please visit our [documentation TODO](TODO).

## Getting Started

Check out our get started with `tapyr` [blog post TODO](TOOD).

### Using Devcontainer

To ensure a consistent development experience across all environments, we recommend using the [devcontainer](https://code.visualstudio.com/docs/remote/containers) configuration with Visual Studio Code or DevPod for container-based development.

1. **Start the Devcontainer**: Open the project in VS Code and select "Reopen in Container" when prompted, or use the Command Palette (`Ctrl+Shift+P`) and choose "Remote-Containers: Reopen in Container". Alternatively, use [DevPod](https://devpod.sh/) following their instructions.
2. **Activate the virtual environment**:
   ```sh
   poetry shell
   ```
3. **Run the application**:
   ```sh
   shiny run app.py --reload
   ```
4. **Execute tests**:
   ```sh
   poetry run pytest
   ```

*Note*: The Devcontainer might limit some `playwright` features, such as `codegen`. For full functionality, consider a local setup.

### Setting Up Locally with Poetry

For developers preferring a local setup without Devcontainer:

1. **Install pipx**: Ensure pipx is installed for managing isolated CLI apps.
2. **Install Poetry**:
   ```sh
   pipx install poetry
   ```
3. **Clone the repository** and navigate to it.
4. **Install dependencies**:
   ```sh
   poetry install
   playwright install
   ```

*Attention*: Follow any additional steps prompted by `playwright install`.

### Deployment on Posit Connect

Deploy your application to Posit Connect by:

1. **Exporting your API Key**:
   ```sh
   export CONNECT_API_KEY="your_api_key_here"
   ```
2. **Configuring Posit Connect**:
   ```sh
   rsconnect add \
   --api-key $CONNECT_API_KEY \
   --server <MY_CONNECT_URL> \
   --name <SERVER_NAME>
   ```
3. **Deploying**:
   ```sh
   rsconnect deploy shiny -t "Tapyr App" .
   ```

Replace placeholders with your server URL, server name, and API key. Verify the deployment on Posit Connect for successful upload.
