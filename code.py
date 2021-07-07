print('-'*50)
# Программа просить ввести строку
String = input("Input your string : ")
Numbers = []
Words = ''
length=len(String)
print('-'*50)
print('String : ' + String)
k=0
# Программа записує всі числа в одну строку, а слова в іншу
for i in range(length):
    j=String[i]
    if '0' <= j <= '9':
        Numbers.append(int(j))
        k+=1
        i+=1
    else:
        Words+=j
        i+=1
Words+=' '
print('-'*50)
print('Numbers : ' + str(Numbers))
print('String without numbers : ' + Words)
i=0
MaxNumber=0
# На данному етапі, программа знаходить найбільше число в массиві чисел
for i in range(len(Numbers)):
        if Numbers[i]>MaxNumber:
            MaxNumber=Numbers[i]
            i+=1
        else:
            i+=1

Numbers2=[]
i=0
# Всі числа, окрім найбільшого, записуються в окремий массив, в степені свого індексу
for i in range(len(Numbers)):
         if Numbers[i]!=MaxNumber:
              Numbers2.append(Numbers[i]**i)
              i+=1
         else:
              continue

print('-'*50)
# Вивід Максимального значення та чисел після зводження до степеню індексу
print('Max number : ' + str(MaxNumber))
print('Numbers x**i without max : ' + str(Numbers2))
print('-'*50)
# Тут йде ініціалізація строки, в яку ми будемо записувати слова з першою і останньою буквою в верхньому регістрі
# l потрібна для того, щоб запам'ятовувати розсташування першої букви слів в рядку
StringUpper=''
l=0
i=0
# Тут программа змінює на верхній регістр букви, які являються першими і останніми в словах рядка
for i in range(len(Words)-1):
    j=Words[i+1]
    if j==' ':
        StringUpper+=Words[l].upper()
        StringUpper+=Words[l+1:i]
        StringUpper+=Words[i].upper()+' '
        l=i+2
        i+=1
    else:
        i+=1
print('String with upper : ' + StringUpper)
print('-'*50)
input()