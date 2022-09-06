# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

x=int(input('enter numbers of day-> '))
if x>0 and x<6 :
    print('No,working day')
elif x>5 and x<=7 : 
    print('Yes,day off')
elif x<1 or x>7 :
    print('Error')    