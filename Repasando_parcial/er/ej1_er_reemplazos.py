import re,sys,os,glob
"""Escribí un programa que reemplace todas las ocurrencias de espacios,
 guiones bajos y dos puntos por la barra vertical (|)."""
def reemplazar (string):
    return string.replace ("_","|").replace(":","|")
print (reemplazar(":fwvvewvewvew___fevewvwe::fewvew--__few4"))

"""Escribí un programa que reemplace los dos primeros 
caracteres no alfanúmericos por guiones bajos."""
def reemplazar1 (string):
    return (re.sub ("(\W)","_",string,count=2))

print (reemplazar1("452vrw@@@@ij5n32b5@@_CQ__-we--_Fu32b5u32b5h325i3u2b5u2n23345"))


""""Realizá un programa que reemplace los espacios y tabulaciones por punto y coma."""
def reemplazar1 (string):

    return string.replace (" ",";").replace("\t",";")
print (reemplazar1("4   52  vrw@@@@ ij5n32b5@   @_CQ_   _-we--_F    u32b5u32b5h325i3u2b5u2n23345"))
