import pickle
import os
import urllib.request

class DNN:
    url_map = {
        "dnn-tiny": "https://github.com/raj-dev-1-git/n-rex/blob/master/weights/dnn_tiny.pkl"
    }

    def __init__(self, name_or_path="dnn-tiny"):

        if name_or_path in self.url_map:
            filename = f"{name_or_path}.pkl"
            if not os.path.exists(filename):
                print(f"Downloading {name_or_path} weights...")
                urllib.request.urlretrieve(self.url_map[name_or_path], filename)
            path = filename
        else:

            path = name_or_path


        with open(path, "rb") as f:
            obj = pickle.load(f)

        self.sizes = obj.sizes
        self.params = obj.params
        self._obj = obj

    def forward(self, x):
        return self._obj.forward(x)
