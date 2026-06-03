class MetadataDB:
    def __init__(self):
        self.store = []

    def add(self, metadata: dict):
        self.store.append(metadata)

    def get_all(self):
        return self.store

    def filter(self, key, value):
        return [m for m in self.store if m.get(key) == value]
