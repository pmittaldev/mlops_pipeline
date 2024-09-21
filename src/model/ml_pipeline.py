import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
    )
from src.utils.decorators import log_execution, handle_exceptions, measure_time
import logging


class MLPipeline:
    """class for handling the machine learning pipeline operations."""

    def __init__(self, model=None, model_params=None):
        """
        Initializes the machine learning pipeline.
        :param model: model,  Default is LogisticRegression.
        :param model_params: Parameters for the model initialization.
        """
        model_params = model_params or {}
        self.model = model if model else LogisticRegression(**model_params)

    @log_execution
    @handle_exceptions
    @measure_time
    def preprocess(self, data: pd.DataFrame, target_column: str) -> tuple:
        """
        Preprocesses the dataset by splitting features and target and then
        splitting the data into training and test sets.
        :param data: A pandas DataFrame containing the features and target.
        :param target_column: The name of the target column in the DataFrame.
        :return: X_train, X_test, y_train, y_test
        """
        X = data.drop(columns=[target_column])
        y = data[target_column]
        return train_test_split(X, y, test_size=0.2, random_state=42)

    @log_execution
    @handle_exceptions
    @measure_time
    def train(self, X_train: pd.DataFrame, y_train: pd.Series) -> None:
        """Trains the model using the provided training data."""
        logging.info("Training the model...")
        self.model.fit(X_train, y_train)
        logging.info("Training completed.")

    @log_execution
    @handle_exceptions
    def evaluate(self, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
        """Evaluates the model and returns several performance metrics."""
        predictions = self.model.predict(X_test)
        metrics = {
            "accuracy": accuracy_score(y_test, predictions),
            "precision": precision_score(y_test, predictions, average="macro"),
            "recall": recall_score(y_test, predictions, average="macro"),
            "f1_score": f1_score(y_test, predictions, average="macro"),
        }
        return metrics
