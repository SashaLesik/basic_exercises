# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])



# Вывести количество букв "а" в слове
word = 'Архангельск'
w = word.lower()
print(w.count("а"))
print("---")


# Вывести количество гласных букв в слове
words = 'Архангельск'
vowels = ["а","у","о","и", "э", "ы", "я", "ю", "е","ё"]
count = 0
for vowel in words:
    if vowel.lower() in vowels:
        count+=1
print(count)
print("---")



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
s = sentence.split(' ')
print(len(s))
print("---")


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
s= sentence.split(' ')
print(s)
for word in s:
    print(word[0])




# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
s= sentence.split(' ')
length_count = 0
for word in s:
    count = len(word)
    length_count = length_count + count
print(length_count/len(s))