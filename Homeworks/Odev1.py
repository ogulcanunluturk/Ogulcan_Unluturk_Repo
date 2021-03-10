list_odd = [1,3,5,7,9]
list_even = [2,4,6,8,10]
result_list = list_odd + list_even
final_list = [element * 2 for element in result_list]
for i in final_list:
  print(i,type(i))