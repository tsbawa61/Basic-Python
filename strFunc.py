# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 06:26:13 2019

@author: Admin
"""

s1='the quick brown fox'
s2='NIELIT'
s3=s1.capitalize()
print(s2.center(10))
print(s2.center(11,'*'))
print(s2.count('I',0,len(s2)))
print(s2.endswith('IT',0,len(s2)))
print(s2.find('IT',0,len(s2)))
print(s2.find('IT',0,len(s2)))
print(s2.find('A',0,len(s2)))
print('\n'.isalnum())
print('\t'.isalnum())
print('a1'.isalnum())
print('a1@'.isalnum())
print('\t'.isspace())
print('a8ssss'.islower())
print('Nielit Kurukshetra'.istitle())
print('nielit Kurukshetra'.istitle())
print(max(s1))
print(s2.replace('I','A'))
print(s2.replace('I','A',1))
print(s2.rfind('I',0,len(s2)))
print(s2.rjust(11,'*'))
print('abcd    '.rstrip())
print(s2.split('I'))
print(s2.split('I',1))
print('abc\ndef\n123'.splitlines())
print(s2.startswith('NI',0,len(s2)))
print(chr(97))
print(chr(97-32))
print(ord('a'))
print(ord('Z'))
print('aBcD12'.swapcase())
print(s1.title())
print('  123'.zfill(10))
print('34523'.isdecimal())
print('345.23'.isdecimal())
