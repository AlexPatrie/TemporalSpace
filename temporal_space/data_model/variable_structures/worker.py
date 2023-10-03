class Worker:
    def __init__(self, context):
        self.context = self.generate_context(context)

    @staticmethod
    def generate_context(c):
        return c
