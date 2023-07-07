a = { "Set":"Set is a collection of elements","Class":"Class is a collection of objects that contains characteristic and behavior","Behavior":"Functions","Characteristic":"Data Type","Data":"Collectoin of row facts","Information":"Meaning full data is called information"}
print(a.keys())
n=str(input("Enter any word from dictionary:"))
print("This is your word",n)
print("This is meaning:",a[n])