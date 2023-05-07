import os,sys,glob,re
def numeros_capital_federal (carpeta1):
    os.mkdir (carpeta1)
    os.chdir (carpeta1)
    with open ("archivo1.txt","a") as arch1:
        arch1.write("643262462352362463262+46+423crnewuvpn3t42+3235523+verw+5491142342353532mcwiromvvwrwrvervwr43v4*3")
    with open ("archivo2.txt","a") as arch2:
        arch2.write ("64326246235236bwrbew+54911542263632623r246326vew2+46+423crneevwwuvpnew3tvew42+3235523+verw+5491v142342353532mcwiromvvwrwrvervwr43v4*3")
    txt=glob.glob("*.txt")
    archivos_leidos=[]
    for archivos_en_lista in txt:
        with open (archivos_en_lista, "r") as arch_list:
            archivos_leidos.append(arch_list.read()) 
    archivos_leidos_completoStr="".join(archivos_leidos)
    lista_con_numeros=re.findall (r"([+]54911[0-9]{8})",archivos_leidos_completoStr)
    print (lista_con_numeros)  
    lista_con_numerosStr="\n".join (lista_con_numeros)  
    os.mkdir ("./Telefonos")
    os.chdir ("./Telefonos")
    with open ("archivo_telefonos.txt","a") as archtel:
        archtel.write (lista_con_numerosStr)
numeros_capital_federal("./Repasando_parcial/CarpertaParcial")
