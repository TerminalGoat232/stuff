
import time as t
from math import *
def tmdprintf(dat, speed):
	for x in str(dat):
		print(x, end='')
		t.sleep(speed)
def tmdprint(dat1, speed1):
	for x1 in str(dat1):
		print(x1, end='')
		t.sleep(speed1)
	print('')
def printf(string):
	print(string, end="")
def RposNschar(str1, c):
	lst = list(str1)
	for i in range(0, len(lst)):
		if lst[i] == lst[c]:
			a = ''.join(lst).replace(''.join(lst[c]), '')
			#if c == str() and c == float(): raise Exception('Position Input Must Be Integer Or Byte Not String, Character Or Float')
	return a 
def ReplcChar(str2, c2, rpl):
	lst2 = list(str2)
	for w in range(0, len(lst2)):
		if lst2[w] == lst2[c2]:
			a2 = ''.join(lst2).replace(''.join(lst2[c2]), rpl)
			if len(list(rpl)) > 1: raise Exception("Replace Input Must Be Character Not Integer")
	return a2
def Char(var):
	lst3 = list(var)
	if len(lst3) > 1: raise Exception('This Is Character type not Int, Float or String')
	return  ''.join(lst3)
def CharByte(var2):
	lst4 = list(str(var2))
	if len(lst4) > 1: raise Exception('This Is Character Byte type [from 1 to 9] not Int, Float or String')
	return int(''.join(lst4))
def SortStr(string):
    return ''.join(sorted(string))

def TakeChar(str3,c3):
	lst5 = list(str3)
	return ''.join(lst5[c3])
def Xrt(pw, rl):
	return pow(rl, 1/pw)
def cbrt(rl1):
	return pow(rl1, 1/3)
def str2ASCII(stri):
	for chim in stri:
		print(ord(chim),'',end='')
	print('')
def FindRplChar(string, replacein, replacewith):
	s = list(string)
	for cc in range(0, len(s)):
		if s[cc] == replacein:
			s[cc] = replacewith
		print(''.join(s[cc]),end='')
	print()
def ASCII2str(ASCII):
	ASCII1 = ASCII.split(',')
	for ASCII2 in ASCII1:
		chim = chr(int(ASCII2))
		print(chim, end='')
	print()



	# test zone
FindRplChar('76 244 32 116 104 7857 110 103 32 110 103 7891 105 32 116 114 432 7899 99 32 109 225 121 32 116 237 110 104 32 109 7883 32 98 7883 32 110 103 117 32 224 32 108 109 97 111 32 108 109 97 111 32 100 97 114 107 32 100 97 114 107 32 99 104 101 101 109 115 32 110 117 116 32 114 108 111 102 32 109 108 103 32 109 108 103 32 99 104 101 101 107 105 32 98 114 101 101 107 105  ',' ', ',')
str2ASCII('Lô thằng ngồi trước máy tính mị bị ngu à lmao lmao dark dark cheems nut rlof mlg mlg cheeki breeki')
ASCII2str('99, 111, 110, 104, 101, 111, 57, 57, 49, 49, 49, 49, 49, 48, 49, 48, 52, 49, 48, 49, 49, 49, 49')
ASCII2str('76,244,32,116,104,7857,110,103,32,110,103,7891,105,32,116,114,432,7899,99,32,109,225,121,32,116,237,110,104,32,109,7883,32,98,7883,32,110,103,117,32,224,32,108,109,97,111,32,108,109,97,111,32,100,97,114,107,32,100,97,114,107,32,99,104,101,101,109,115,32,110,117,116,32,114,108,111,102,32,109,108,103,32,109,108,103,32,99,104,101,101,107,105,32,98,114,101,101,107,105')
