from random import shuffle


class Functions():
    # Write a python program which takes 2 numbers and pring true if first is bigger than second
    def is_first_Bigger(self, num1, num2):
        return num1 > num2

    # Write a Python program to get a string from a given String where all occurences of its first char,
    # have been changed to '$',except first char itself
    def char_to_dollar(self, word):
        if(len(word)<1):
            return ""
        return word[0:1] + word[1:].replace(word[0], '$')
    #Write a Python program to shuffle and print a specified list
    def  shuffle_list(self,list):
        shuffle(list)
        return list
    #Given a python list reverse it:
    def reverse_list(self,list):
        list.reverse()
        return list
    #Write a Python program to remove an item from a set if it is present in the set:
    def remove_item(self,my_set,element):
        try:
            my_set.remove(element)
        except Exception as e:
            print("Element doesn't exist:",e)
        return my_set
    #Write a Python program to get the 4th element from the beginning of the tuble and the end"
    def get_fourth_element(self,my_tuple):
        if(len(my_tuple)<4):
            print("tuple length is below 4")
            return
        print("Elements:"+str(my_tuple[3])+","+str(my_tuple[-4]))