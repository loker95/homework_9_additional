def censored_word(text):

    forbidden_word = "die"
    censored_text = text.replace(forbidden_word, '***')
    replacements = text.count(forbidden_word)

    return censored_text, replacements


my_text = ("To be, or not to be, that is the question, "
           "Whether 'tis nobler in the mind to suffer "
           "The slings and arrows of outrageous fortune, "
           "Or to take arms against a sea of troubles, "
           "And by opposing end them? To die: to sleep; "
           "No more; and by a sleep to say we end "
           "The heart-ache and the thousand natural shocks "
           "That flesh is heir to, 'tis a consummation "
           "Devoutly to be wish'd. To die, to sleep.")

new_text, replacements_counter = censored_word(my_text)

print("Замененный текст:")
print(new_text)

print(f"Количество замен: {replacements_counter}")