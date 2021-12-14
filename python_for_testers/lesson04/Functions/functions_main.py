from python_for_testers.lesson04.Functions.my_functions import Functions
func=Functions()
num1=6
num2=5
print("First is bigger than Second:",func.is_first_Bigger(num1,num2))
word="restart"
print("The word:"+word+" is converted to:"+func.char_to_dollar(word))
list=[1,2,3,4,5,6,7,8,9]
print("Original list:"+str(list)+"-->Shuffled:"+str(func.shuffle_list(list)))
alist=[100,200,300,400,500]
print("Original List:"+str(alist)+"-->Reversed:"+str(func.reverse_list(alist)))
my_set = {1, 2, 3, 4}
print("Original Set:"+str(my_set)+"-->Set After Remove:"+str(func.remove_item(my_set,77)))
my_tuple = (1, 2, 3,4,5,6)
func.get_fourth_element(my_tuple)

