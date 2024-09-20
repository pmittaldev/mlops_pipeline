
# Machine Learning Pipeline

---

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Running Terraform](#running-terraform)
- [Running Tests](#running-tests)
- [Running the Jupyter Notebook](#running-the-jupyter-notebook)

---


## Overview

This project implements a machine learning pipeline using the **Facade Pattern**. The pipeline encapsulates the steps for data preprocessing, model training, and evaluation, and presents a simple, easy-to-use interface for these processes. The pipeline is designed to work with the iris dataset and uses **Logistic Regression** for classification tasks.

## Setup

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

3. **Activate the virtual environment**:
   ```bash
    poetry shell
    ```

## Running Terraform

To provision the infrastructure using Terraform, follow these steps:

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

To run tests with Poetry:

1. **Run Tests**:

    After installing the dependencies, you can run the tests using:

    ```bash
    poetry run pytest
    ```

2. **Check Code Formatting**:

    To check code formatting with `black`, use the following command:

    ```bash
    poetry run black --check .
    ```

3. **Format Code**:

    To automatically format the code using `black`, run:

    ```bash
    poetry run black .
    ```
3. **Linting**:

    To check linting using `flake8`, run:

    ```bash
    poetry run flake8 .
    ```

## Running the Jupyter Notebook

1. **Activate the environment if not done already**:
    ```bash
    poetry shell
    ```


2. **Launch Jupyter Notebook**:
    ```bash
    jupyter notebook
    ```
3. **Open and Run the Notebook**:

* Navigate to the notebook/ml_pipeline.ipynb file in the Jupyter interface and open it.
* Follow the instructions in the notebook to run the pipeline. The notebook will walk you through preprocessing, training, and evaluating the model.