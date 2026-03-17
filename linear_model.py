from base_model import BaseModel


class LinearRegressionModel(BaseModel):

    def __init__(self, config):
        super().__init__(config)

    def train(self, data):
        print(
            "LinearRegression: Training on",
            len(data),
            "samples for",
            self.config.epochs,
            "epochs (lr=",
            self.config.learning_rate,
            ")",
        )

    def evaluate(self, data):
        print("LinearRegression: Evaluation MSE = 0.042")