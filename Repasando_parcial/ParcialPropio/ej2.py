import os,sys,glob,re

def caracteres_raros (string):
     return string.replace("&","|").replace("*","|").replace("@","|")
print (caracteres_raros("*&@@@Feve&%$&"))
