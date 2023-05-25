class KeyValueStorage:
    def __init__(self, file_path):
        self.file_path = file_path
        self._data = {}
        with open(file_path, 'r') as f:
            for line in f:
                key, value = line.strip().split('=')
                if value.isdigit():
                    value = int(value)
                elif value.replace('.', '', 1).isdigit():
                    value = float(value)
                if key in self.__dict__:
                    raise ValueError(f"Attribute name '{key}' clashes with a built-in attribute name")
                self._data[key] = value
                setattr(self, key, value)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value
        setattr(self, key, value)
        with open(self.file_path, 'a+') as f:
            f.seek(0)
            lines = f.readlines()
            new = True
            for i, line in enumerate(lines):
                if line.startswith(f"{key}="):
                    lines[i] = f"{key}={value}\n"
                    new = False
                    break
            if new:
                lines.append(f"{key}={value}\n")
            f.seek(0)
            f.truncate()
            f.writelines(lines)

    def __delitem__(self, key):
        del self._data[key]
        delattr(self, key)

    def __contains__(self, key):
        return key in self._data

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data.items())

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()
