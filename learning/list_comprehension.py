'''
	List comprehension example
'''
a=[1,34,54,23,-67,-88,-90,9,15,6,3]
mynewlist=[ele for ele in a if ele%2==0] #adding elements to a new list only if they are even
print(mynewlist)
