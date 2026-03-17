from model_config import ModelConfig
from linear_model import LinearRegressionModel
from neural_model import NeuralNetworkModel
from data_loader import DataLoader
from trainer import Trainer
from base_model import BaseModel


data = [1, 2, 3, 4, 5]

loader = DataLoader(data)

config1 = ModelConfig("LinearRegression", 0.01, 10)
config2 = ModelConfig("NeuralNetwork", 0.001, 20)

print(config1)
print(config2)

model1 = LinearRegressionModel(config1)
model2 = NeuralNetworkModel(config2, [64, 32, 1])

print("Models created:", BaseModel.model_count)

trainer1 = Trainer(model1, loader)
trainer1.run()

trainer2 = Trainer(model2, loader)
trainer2.run()