
import tensorflow as tf
from tensorflow import keras
from .browser import InternetBrowser
from .github_integration import GithubIntegration

class AIAgent:
    def __init__(self):
        self.model = self._build_model()
        self.browser = InternetBrowser()
        self.github = GithubIntegration()

    def _build_model(self):
        model = keras.Sequential([
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(32, activation='relu'),
            keras.layers.Dense(1, activation='sigmoid')
        ])

        model.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])

        return model

    def train(self, data, labels):
        self.model.fit(data, labels, epochs=5)

    def predict(self, data):
        return self.model.predict(data)

    def browse_internet(self, url):
        return self.browser.browse(url)

    def integrate_github(self, repo_url):
        return self.github.integrate(repo_url)
