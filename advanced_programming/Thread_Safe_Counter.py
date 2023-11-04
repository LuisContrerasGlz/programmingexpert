"""

Write a WordCounter class that is meant to be able to count words in large texts, so that a user of that class can quickly calculate how many times a specific word occurs in a string.

WordCounter should implement the following methods:

process_text(text) should take in a string, text, and update the internal attributes of WordCounter in a thread-safe manner. You may assume naively that text.split(" ") is good enough to return the list of words in the passed text.

get_word_count (word) should take in a string, word, and check how many times that word has been seen in all the texts that this WordCounter has processed. If this word has never been seen, you should return

NOTE: This class must be thread-safe; meaning that many threads should be able to use the WordCounter at the same time, and the calculations must remain accurate as if only a single thread was using the instance of WordCounter.

NOTE: You may not use the Counter class of the collections standard library 

"""

import threading


class WordCounter:
    def __init__(self):
        self.lock = threading.Lock()
        self.word_counts = {}

    def process_text(self, text):
        words = text.split(" ")
        temporary_word_counts = {}
        for word in words:
            if word not in temporary_word_counts:
                temporary_word_counts[word] = 0
            temporary_word_counts[word] += 1
        self._increase_word_counts(temporary_word_counts)

    def get_word_count(self, word):
        self.lock.acquire()
        count = self.word_counts.get(word, 0)
        self.lock.release()
        return count

    def _increase_word_counts(self, word_counts):
        self.lock.acquire()
        for word in word_counts:
            self.word_counts[word] = self.word_counts.get(
                word, 0) + word_counts[word]
        self.lock.release()
