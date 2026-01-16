#https://www.youtube.com/watch?v=ix9cRaBkVe0
#print("Hello World")

#first_name = input("Enter your first name: ")
#last_name = input("Enter your last name: ")

#print("Hello " + first_name + " " + last_name)
#print(f"Hello {first_name} {last_name}")
#Output: print
#Format: f
#Data types: string, integer, float, boolean (True/False)
#Typecast: str(), int(), float(), bool()
#Input function: input()
#Arithmertic operators: + , - , / , * , ** , %
#math functions: round, abs, pow(x, y), max(x,y,z), min(x,y,z)
#import libraries: import <lib> e.g. math, time
#import math: math.pi, math.e, math.sqrt(x), math.ceil(x), math.floor(x)
#import time: time.sleep(3)
#import random: randint(1,6), random(), choice(tuple), shuffle(list)
#Conditional stmts: if <cond>:
#                      <1>
#                   elif <cond>:  elif <cond> is not None:
#                      <2>
#                   else:
#                       <3>
# comparison operators: >=, ==,
#logical operators: or, and, not
#conditional expression: ternary operator, print or assign. e.g A = X if <cond> else Y
#string methods: len(x), find(x) - first occurrence, rfind(x) - last occurrence,
#                x.capitalize(), x.upper(), x.lower(), x.isdigit(), x.isalpha(), x.count(y)
#                x.replace(y,z)
#help(str) - all helper methods of string
# indexing - start, end, step using [start:end:step] - [:end],[start:],[::step][-end:]
#reverse a string - [::-1]
#format specifiers - {value:flags} e.g. print({price:.2f})
#{val:.(number)f},{val:10},{val:010},{val:+},{val:<},{val:>},{val:^},{val:=},{val: },{val:,},{val:+,.2f}
#while: while <cond>:
#          stmt1
#          stmt2
#       print(f"Hello {first_name} {last_name}")
# while not <cond>:
# while True:
#     break
#for loops:  for x in range(1,11):
#               print(x)
#for loops:  for x in range(1,11, 2):
#               print(x)
#for loops:  for x in reverse(range(1,11)):    range(11,1,-1):
#               print(x)
#for loops:  for x in <string>:
#               print(x)
#for loops:  for x in range(1,11):
#        if x == 13:         if x == 13:
#           continue            break
#        print(x)            print(x)
#nested loop - outer loop:
#                  inner loop:
#print(x, end:"") - same line
#collections: List [], Set(immutable, no duplicates,add/remove) {}, Tuple(Faster) () , print(array[0:3])
# methods in collections: print(dir(<collection>), print(help(<collection>)
#List collection functions: len, in, append, remove, insert(index,val), sort, reverse, clear,index, count
#Set: len,in, pop,add,remove
#Tuple: count,index,len,in
#2-dimensional list: [list1,list2,list3]
#dictionary: {key:value} ordered and changeable
#dictionary methods: get() - None if not found, update(key,value), pop(key), popitem(), clear(), keys(), values(), items()
#help, dir for dictionary
#functions: def function_name(<param>):
#                stmt1
#                 return a
#function argument types: positional, DEFAULT, keyword, arbitrary
#default arg: def function_name(x,y=1,z=2)
#keyword args: pass arg name in function call: function_name(x,y=1,z=2)
#arbitrary args: *args, **kwargs : function_name(*args) - tuple, f_name(**kwargs) - dict: keys,values,items,get
# f_name(*args,**kwargs)
#Iterables : List, Tuples, Set, Dict
#Membership operators in string,list,set,tuples,dict: in, not in
#List comprehension: expression for value in iterable if <cond> . doubles = [<list comprehension]
#match-case stmts(switch): match <case>:
#                               case 1|2:
#                                   return a
#                               case _:
#                                   return default
#module: built-in, custom module (import library): import <module> as <nick_name>, from <module> import <function>
#variable scope, scope resolution: Local -> Enclosed -> Global ->Built-in
#if __name__ == "__main__":
#    main()
#object, class: class <class_name>:
#                   def __init__(self,<instance_variables>):
#               c = <class_name>(args)
#               print(c.arg1)
#from <filename> import <class_name>
#class_variables: static var
#Inheritance: class Child(Parent) , class Sub(Super)
#multiple inheritance: class Child(Parent1,Parent2)
#multi level inheritance: A -> B(A) -> C(B)
#super(): super().__init__(args)
#Polymorphism: Inheritance, Duck Typing
#abstract method: from abc import ABC,abstractmethod
#                 @abstractmethod
#                 def <method_name>:
#static methods, instance methods: @staticmethod
#                                   def funct_name:
#class methods: @classmethod
#               def <f_name>(cls):
#Magic methods: def __init__(self,args):, def __str__(self):, def __eq__(self,other):, def __lt__(self,other):, def __gt__(self,other):,
#               def __add__(self,other):,def __contains__(self,keyword):, def __getitem__(self,key):
#@property methods: Decorator for method as property . <object>.<property method>
#setter,getter,deleter: @<attribute>.setter , @<attribute>.deleter
#Decorator: def <decorator func>(func):
#                def wrapper(*args,**kwargs):
#                   funct(*args,**kwargs)
#                return wrapper
#exception: try, except, finally , ZeroDivisionError, TypeError, ValueError
#  try:
#     stmt1
#  except ValueError:
#  finally:
#file detection: import os , os.path
#writing files: with open(<file_path>,'w') as file:    w,x,a,r
#                       file.write()
#multithreading: import threading
#                 t = threading.Thread(target=my_function)
#                  t.start()
#                  t.join()
#APIs: import requests (install)
#PyQt5: GUI
#import numpy as np
#print(np.__version__)
import pandas as pd

data = {
    "Name" : ["A" , "B", "C", "D"],
    "Age" : [25, 30, 35, 40],
    "City" : ["New York", "London", "Paris", "Tokyo"]
}

result = pd.DataFrame(data)
print(result)

dataList = [
    ["A", 25, "New York"],
    ["B", 30, "London"],
    ["C", 35, "Paris"],
    ["D", 40, "Tokyo"]
]

result1 = pd.DataFrame(dataList, columns=["Name", "Age", "City"])
print(result1)

dataDict = [
    {"Name": "A", "Age": 25, "City": "New York"},
    {"Name": "B", "Age": 30, "City": "London"},
    {"Name": "C", "Age": 35, "City": "Paris"},
    {"Name": "D", "Age": 40, "City": "Tokyo"}
]


result2 = pd.DataFrame(dataDict)
print(result2)