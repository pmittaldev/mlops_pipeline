
# Machine Learning Pipeline (MLPipeline)

---

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Running Terraform](#running-terraform)
- [Running Tests](#running-tests)
- [Running Jupyter Notebook](#running-notebook)
- [Running CI](#running-ci)

---

## Overview

This project implements a machine learning pipeline using the **Facade Pattern**. The pipeline encapsulates the steps for data preprocessing, model training, and evaluation, and presents a simple, easy-to-use interface for these processes. The pipeline is designed to work with the iris dataset and uses **Logistic Regression** for classification tasks.

### Prerequisites

* Ensure that **Python 3.11 or above** is installed on your system and configured as `python3`. You can check the installed version with:
  ```bash
  python3 --version

## Setup

* Make sure python 3.11 or above is installed on the system and configured with python3

This project uses [Poetry](https://python-poetry.org/) to manage dependencies and virtual environments.

1. **Install Poetry**:

   You can install Poetry by running:

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Install Dependencies**:
    ```bash
    poetry install
    ```
2. **Activate Shell**:
    ```bash
    poetry shell
    ```

## Running Terraform

To provision the infrastructure using Terraform, follow these steps:

change the directory to /terraform

1. **Initialize Terraform**:

    In the Terraform project directory, run:

    ```bash
    terraform init
    ```

2. **Plan the Infrastructure**:

    To check the changes Terraform will apply, run:

    ```bash
    terraform plan
    ```

3. **Apply the Infrastructure**:

    To apply the changes and provision the infrastructure, run:

    ```bash
    terraform apply
    ```

## Running Tests

To run tests and Linting with Poetry:

1. **Run Tests**:

    After installing the dependencies, you can run the tests using:

    ```bash
    poetry run pytest
    ```

2. **Run linting**:

    To run flake8 linter use the following command:

    ```bash
    poetry run flak8 .
    ```


## Running Notebook

1. **Activate enviroment if not yet done**
    ```bash
    poetry shell
    ```

2. **Activate enviroment if not yet done**
Launch Jupyter Notebook

    ```bash
    jupyter notebook
    ```

This will open a new browser window with the Jupyter interface.

3. **Open and Run the Notebook**:
   
    * Navigate to the notebook/ml_pipeline.ipynb file in the Jupyter interface and open it.
    * Follow the instructions in the notebook to run the pipeline. The notebook will walk you through preprocessing, training, and evaluating the model.

## Running CI

The CI workflow to run the pytest and the linting is present under .github/workflows. The CI will get trigger on creating the pull request to the main branch. 