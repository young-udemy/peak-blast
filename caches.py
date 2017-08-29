class DictCache:

    def __init__(self):
        self.data = {}

    def flush(self):
        self.data = {}

    def get(self, namespace, key):
        try:
            return self.data[namespace][key]
        except KeyError:
            return None

    def set(self, namespace, key, value):
        if namespace not in self.data:
            self.data[namespace] = {}
        self.data[namespace][key] = value
