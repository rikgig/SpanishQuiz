import streamlit as st
import random
from quiz import Quiz
from quiz_functions import read_word_dictionary_from_csv, quiz_student, binary_to_text



def main():
    st.title("French to Spanish Quiz")
    questions_asked = st.session_state.get('questions_asked', 0)
    file_loaded = st.session_state.get('file_loaded',False)
    words_dictionary = st.session_state.get('words_dictionary',None)
    theQuiz = st.session_state.get('theQuiz',Quiz())
    french_words = st.session_state.get('french_words',None)

    words_dictionary = None


    if file_loaded == False:
        uploaded_file = st.file_uploader("Upload CSV file with word pairs (French, Spanish)", type="csv")

        if uploaded_file is not None:
            print("loading file")

            words_dictionary = read_word_dictionary_from_csv(binary_to_text(uploaded_file))
            theQuiz.spanish_words = list(words_dictionary.keys())[1:10]
            theQuiz._words_dictionary = words_dictionary
            random.shuffle(theQuiz.spanish_words)
            st.session_state['file_loaded'] = True
            st.session_state['theQuiz'] = theQuiz
    else:
        words_dictionary = st.session_state['theQuiz']._words_dictionary
        spanish_words = st.session_state['theQuiz'].spanish_words
        print(st.session_state)
    if words_dictionary and len(words_dictionary) > 0:
        if questions_asked < 10:
            questions_asked = quiz_student(st, theQuiz)
        else:
            st.write("Quiz Completed: 10 questions asked.")
    else:
        st.write("No word pairs found. Upload a valid csv file.")


if __name__ == "__main__":
    main()
