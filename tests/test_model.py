import pytest
import pandas as pd
from src.model.ml_pipeline import MLPipeline


@pytest.fixture
def sample_data():
    """Fixture that returns a simple dataset for testing."""
    data = {
        "SepalLengthCm": [5.1, 6.8, 4.7, 4.6, 5.0],
        "SepalWidthCm": [3.5, 2.8, 3.2, 3.1, 3.6],
        "PetalLengthCm": [1.4, 4.8, 1.3, 1.5, 1.4],
        "PetalWidthCm": [0.2, 1.4, 0.2, 0.2, 0.2],
        "Species": [
            "Iris-setosa",
            "Iris-versicolor",
            "Iris-virginica",
            "Iris-versicolor",
            "Iris-versicolor",
        ],
    }
    return pd.DataFrame(data)


@pytest.fixture
def pipeline():
    return MLPipeline()


def test_preprocess(pipeline, sample_data):
    """Test that preprocessing correctly scales the data."""
    X, y = pipeline.preprocess(sample_data, "Species")
    # Check that the target column is properly extracted
    assert "Species" not in X.columns

    # Check that the scaling worked (all values should have been transformed)
    assert (X.values.mean() < 1e-7) and (X.values.std() - 1 < 1e-7)


def test_train(pipeline, sample_data):
    """Test that the training function works correctly."""
    X, y = pipeline.preprocess(sample_data, "Species")
    X_test, y_test = pipeline.train(X, y)
    # Check that the test data is returned properly
    assert X_test.shape[0] == 1
    assert y_test.shape[0] == 1


def test_evaluate(pipeline, sample_data):
    """Test that the evaluation returns an accuracy score."""
    X, y = pipeline.preprocess(sample_data, "Species")
    X_test, y_test = pipeline.train(X, y)
    # Evaluate the model
    accuracy = pipeline.evaluate(X_test, y_test)
    assert accuracy == 1.0
