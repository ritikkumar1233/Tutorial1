a = [3, 6, 9, 12, 15, 18, 21]  
b = [4, 8, 12, 16, 20, 24, 28]  
odd_index_list = [num for index, num in enumerate(a) if index % 2]  
print("Element at odd-index positions from list one")  
print(odd_index_list)  
even_index_list = [num for index, num in enumerate(b) if not index % 2]  
print("Element at even-index positions from list two")  
print(even_index_list)  
final_list = odd_index_list + even_index_list  
print("Printing Final third list")  
print(final_list)
