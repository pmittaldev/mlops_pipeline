import pytest
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from src.model.ml_pipeline import MLPipeline


@pytest.fixture
def iris_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df["target"] = iris.target
    return df


@pytest.fixture
def pipeline():
    """Fixture to initialize the MLPipeline with LogisticRegression."""
    return MLPipeline(model=LogisticRegression())


@pytest.fixture
def processed_data(iris_data, pipeline):
    """Fixture to preprocess the Iris data using MLPipeline."""
    return pipeline.preprocess(iris_data, "target")


def test_preprocessing(processed_data):
    """Test the preprocessing step of MLPipeline."""
    X_train, X_test, y_train, y_test = processed_data
    # Assert that training and testing sets are not empty
    assert len(X_train) > 0
    assert len(X_test) > 0
    assert len(y_train) > 0
    assert len(y_test) > 0


def test_training(pipeline, processed_data):
    """Test the training step of MLPipeline."""
    X_train, X_test, y_train, y_test = processed_data
    # Train the model and ensure no exceptions are raised
    pipeline.train(X_train, y_train)
    # Check model has been trained (LogisticRegression uses 'coef_' attribute)
    assert hasattr(pipeline.model, "coef_")


def test_evaluation(pipeline, processed_data):
    """Test the evaluation step of MLPipeline."""
    X_train, X_test, y_train, y_test = processed_data
    # Train the model before evaluation
    pipeline.train(X_train, y_train)
    # Evaluate the model
    metrics = pipeline.evaluate(X_test, y_test)
    # Ensure the metrics are calculated correctly
    assert "accuracy" in metrics
    assert "precision" in metrics
    assert "recall" in metrics
    assert "f1_score" in metrics
    # Check that accuracy is within a reasonable range
    assert metrics["accuracy"] > 0.5
