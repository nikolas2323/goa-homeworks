#შექმენით სია, რომელშიც დაამატებთ მნიშვნელობას სიის ბოლოში, შემდეგ ამოშლით ნებისმიერ მნიშვნელობას
# და მაგის შემდგომ  გაიგებთ ამ სიაში არსებული მნიშვნელობების
# რაოდენობას და შემდეგ ჩაამატებთ ახალ მნიშვნელობას მეორე ინდექსზე 

list_groceries = ['bread', 'milk', 'flour', 'eggs']

list_groceries.append('water')

list_groceries.pop(3)

list_groceries.insert(1,"tomatoes")

print(len(list_groceries))

print(list_groceries)
