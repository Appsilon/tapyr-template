# PyShiny Dashboard Template

This template offers a streamlined way to create and deploy Shiny applications using Python. It leverages `poetry` for dependency management and `playwright` for app testing, facilitating both local development and deployment on Posit Connect.

## Getting Started

### Using Devcontainer

For a seamless development experience, we recommend using the provided [devcontainer](https://code.visualstudio.com/docs/remote/containers) configuration with Visual Studio Code. This setup encapsulates the development environment, ensuring consistency across machines.

1. **Start the Devcontainer**: Either use [DevPod](https://devpod.sh/) or open the project in VS Code, and when prompted, reopen it in a container. Alternatively, use the Command Palette (`Ctrl+Shift+P`) and select "Remote-Containers: Reopen in Container". Wait for the container to set up.
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

*Note*: The Devcontainer environment may limit the use of `playwright` browser features, such as `codegen`. For these features, consider setting up the project locally.

### Setting Up Locally with Poetry

For local development without Devcontainer, follow these steps:

1. **Install pipx**: [pipx](https://github.com/pypa/pipx) allows you installing CLI apps in isolated environments. This is how we want to install the `poetry`.
1. **Install Poetry** using `pipx`:
   ```sh
   pipx install poetry
   ```
2. **Clone the repository** and navigate to the project directory.
3. **Install dependencies**:
   ```sh
   poetry install
   playwright install
   ```

*Attention*: The `playwright install` command may prompt additional steps. Follow the instructions provided in the terminal.

### Deployment on Posit Connect

Deploy your Shiny application to Posit Connect with the following steps:

1. **Export your Posit Connect API Key**:
   ```sh
   export CONNECT_API_KEY="your_api_key_here"
   ```
2. **Configure Posit Connect** with your server details:
   ```sh
   rsconnect add \
   --api-key $CONNECT_API_KEY \
   --server <MY_CONNECT_URL> \
   --name <SERVER_NAME>
   ```
3. **Deploy the application**:
   ```sh
   rsconnect deploy shiny -t "PyShiny Template" .
   ```

Replace placeholders (`<MY_CONNECT_URL>`, `<SERVER_NAME>`, and `your_api_key_here`) with your actual Posit Connect server URL, desired server name, and API key.
