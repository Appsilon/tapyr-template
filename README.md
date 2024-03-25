# `tapyr` - PyShiny Dashboard Template

Effortlessly create and deploy Shiny applications using Python with our PyShiny Dashboard Template.
Designed for developers seeking a seamless transition from development to deployment, this template utilizes `poetry` for dependency management and `pytest`/`playwright` for comprehensive app testing.
Ideal for projects aiming for high-quality code and efficient deployment on Posit Connect.

## Getting Started

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
   rsconnect deploy shiny -t "PyShiny Template" .
   ```

Replace placeholders with your server URL, server name, and API key. Verify the deployment on Posit Connect for successful upload.

## Features

Our template ensures a streamlined development lifecycle, offering:

- **Modular Package Structure**: Clean, maintainable code organization.
- **Dependency Management with Poetry**: Easy handling and setup of virtual environments.
- **Testing Frameworks**: `pytest` for unit tests and `playwright` with `pytest-playwright` for automated end-to-end testing.
- **Consistent Devcontainer Setup**: Eliminates "works on my machine" issues.
- **Code Quality Assurance**:
  - `pre-commit` for clean commits.
  - `ruff` for linting (`ruff check`) and formatting (`ruff format`).
  - `pytest-cov` to monitor test coverage.
  - `bandit` for security checks.
- **Continuous Integration**: Automated checks via GitHub Actions.
- **Structured Logging with Loguru**: Enhanced debugging and monitoring.
- **Best Practice Configuration**: Using `pydantic-settings`.
- **Efficient Deployment**: Smooth deployment to Posit Connect with `rsconnect`.
- **Static Type Checking with mypy**: Ensures type safety and code quality.

## Community and Contributions

We welcome contributions, feedback, and questions to improve this template. Please feel free to open an issue or submit a pull request on our GitHub repository.
