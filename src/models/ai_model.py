
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

class AIModel:
    def __init__(self, max_words=10000, embedding_dim=100, max_sequence_length=100):
        self.max_words = max_words
        self.embedding_dim = embedding_dim
        self.max_sequence_length = max_sequence_length
        self.tokenizer = Tokenizer(num_words=self.max_words, oov_token="<OOV>")
        self.model = self.build_model()

    def build_model(self):
        model = Sequential([
            Embedding(self.max_words, self.embedding_dim, input_length=self.max_sequence_length),
            LSTM(128, return_sequences=True),
            LSTM(128),
            Dense(64, activation='relu'),
            Dense(self.max_words, activation='softmax')
        ])
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def train(self, sequences, labels, epochs=100, validation_split=0.2):
        self.model.fit(sequences, labels, epochs=epochs, validation_split=validation_split)

    def generate_text(self, seed_text, num_words_to_generate):
        for _ in range(num_words_to_generate):
            token_list = self.tokenizer.texts_to_sequences([seed_text])[0]
            token_list = pad_sequences([token_list], maxlen=self.max_sequence_length-1, padding='pre')
            predicted = self.model.predict_classes(token_list, verbose=0)
            output_word = ""
            for word, index in self.tokenizer.word_index.items():
                if index == predicted:
                    output_word = word
                    break
            seed_text += " " + output_word
        return seed_text
