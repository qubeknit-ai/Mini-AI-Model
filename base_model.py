class BaseModel:

    model_count = 0

    def __init__(self, config):
        self.config = config
        BaseModel.model_count += 1

    def train(self, data):
        raise NotImplementedError

    def evaluate(self, data):
        raise NotImplementedError