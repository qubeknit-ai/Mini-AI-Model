from base_model import BaseModel


class NeuralNetworkModel(BaseModel):

    def __init__(self, config, layers):
        super().__init__(config)
        self.layers = layers

    def train(self, data):
        print(
            "NeuralNetwork",
            self.layers,
            ": Training on",
            len(data),
            "samples for",
            self.config.epochs,
            "epochs (lr=",
            self.config.learning_rate,
            ")",
        )

    def evaluate(self, data):
        print("NeuralNetwork: Evaluation Accuracy = 91.5%")