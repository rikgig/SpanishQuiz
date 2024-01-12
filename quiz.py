

class Quiz:
    _words_dictionary = None
    spanish_words = None
    currentWord = ""
    questions_asked = 0
    word_index = 0

    def pick_a_word(self):
        print(f"Items in the word list: {len(self.spanish_words)}")
        spanish_word = ""
        while len(spanish_word) == 0:
            spanish_word = self.spanish_words[self.word_index]
            self.word_index += 1
        self.currentWord = spanish_word
        return self.currentWord

    def set_words_dictionary(self, value):
        self._words_dictionary = value

    def set_questions_asked(self, value):
        self.questions_asked = value