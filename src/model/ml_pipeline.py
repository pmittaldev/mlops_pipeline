import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from src.utils.decorators import log_execution, handle_exceptions, measure_time


class MLPipeline:
    """class for handling the machine learning pipeline operations."""

    def __init__(self):
        self.model = LogisticRegression()
        self.scaler = StandardScaler()

    @log_execution
    @handle_exceptions
    @measure_time
    def preprocess(self, data: pd.DataFrame, target_column: str):
        """Preprocesses the data by scaling features."""
        X = data.drop(columns=[target_column])
        y = data[target_column]
        X_scaled = self.scaler.fit_transform(X)
        return pd.DataFrame(X_scaled, columns=X.columns), y

    @log_execution
    @handle_exceptions
    @measure_time
    def train(self, X: pd.DataFrame, y: pd.Series):
        """Trains the Logistic Regression model."""
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        self.model.fit(X_train, y_train)
        return X_test, y_test

    @log_execution
    @handle_exceptions
    @measure_time
    def evaluate(self, X_test: pd.DataFrame, y_test: pd.Series):
        """Evaluates the model on test data."""
        predictions = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        return accuracy
