class Trainer:

    def __init__(self, model, dataloader):
        self.model = model
        self.dataloader = dataloader

    def run(self):
        data = self.dataloader.get_data()

        print("\n--- Training", self.model.config.model_name, "---")

        self.model.train(data)
        self.model.evaluate(data)