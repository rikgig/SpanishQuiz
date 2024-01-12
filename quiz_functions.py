import csv
from io import StringIO
from unidecode import unidecode

def read_word_dictionary_from_csv(file):
    word_dict = {}
    with file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 2:
                genre_es, es, genre_fr, fr, category, details, = row
                word_dict[es.strip()] = fr.strip()
    return word_dict

def remove_accents(text):
    return unidecode(text)

def check_accent(user_input, correct_translation):
    user_input_normalized = remove_accents(user_input.lower())
    correct_translation_normalized = remove_accents(correct_translation.lower())
    
    if user_input_normalized == correct_translation_normalized:
        return "Correct"
    elif user_input.lower() == correct_translation.lower():
        return "Warning: Accents are incorrect"
    else:
        return "Wrong"

def quiz_student(st, theQuiz):
    
    if theQuiz.questions_asked < 1:
        st.write("\nLet's start the quiz!\n")
    
    if theQuiz and theQuiz.questions_asked < 10:
        print(f"Session state before: {st.session_state}")
        spanish_word = theQuiz.pick_a_word()
        print(f"Session state after: {st.session_state}")
        user_input = st.text_input(f"Translate '{spanish_word}' to French:", key="translatedWordText")
        print(f"Session state after text_input: {st.session_state}")
        user_input = st.session_state['translatedWordText']
        print("User input read: " + user_input)
        if user_input:  

            correct_translation = theQuiz._words_dictionary[spanish_word]
            result = check_accent(user_input, correct_translation)
        
            st.write(result)
            if result != "Correct":
                st.write(f"The correct translation is '{correct_translation}'.")
        
            theQuiz.questions_asked = theQuiz.questions_asked+1
        else:
            print("fill the text!")    
    return theQuiz.questions_asked


def binary_to_text(binary_file):
    data = StringIO(binary_file.getvalue().decode("utf-8"))
    return data

