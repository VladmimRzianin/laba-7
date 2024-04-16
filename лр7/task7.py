text = str(input("Введите текст ")) 
vowels = 0 
consonants = 0 
vowel = set("аеиоуыэюяАЕИОУЫЭЮЯ") 
consonant = set("йцкнгшщзхъфвпрлджчсмтьбЙЦКНГШЩЗХЪФВПРЛДЖЧСМТБЬ") 
for letter in text: 
    if letter in vowel: 
        vowels += 1 
    if letter in consonant: 
        consonants += 1 
print("Количество гласных = ", vowels) 
print("Количестов согласных = ", consonants)