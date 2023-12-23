# `cookiecutter-minimal-python` 🎬

## Description 🖼️

The repository implements a **Cookiecutter template for creating a minimal Python 3 project**, with an MIT license, having the following **tools**:

- **Poetry** for dependency management;
- **Ruff** for linting and import sorting;
- **Black** for automatic formatting;
- **pytest** for unit testing;
- **Coverage.py** for coverage tracking; and
- **Poe** for task running.

**Visual Studio Code**'s configuration already contains the required integration with the above tools. In addition, the generated project recommends IDE **extension**. You can install them to ease the development.

## Setup 🛠️

1. [Install Cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html).
2. Clone the repository with `git clone https://github.com/iosifache/cookiecutter-minimal-python`.
3. Enter the cloned folder.
4. Fill `cookiecutter.json` with the details of your project.
5. Generate a new project with `cd .. && cookiecutter --no-input cookiecutter-minimal-python`.
6. Enter the generated project in the current folder.
7. Install project's dependencies with `poetry install`.
