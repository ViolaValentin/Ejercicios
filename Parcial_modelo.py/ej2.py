import glob,os,sys,re
def mails_secretos ():
    os.chdir ("C:\\Users\\valen\\Ejercicios\\Parcial_modelo.py\\carpeta_con_txt")
    txt=glob.glob ("*.txt")
    for archivo in txt:
        with open (archivo,"r") as arch:
            todos_los_mails=arch.read()
            mails_en_lista= (re.findall (r"[a-z0-]+[._-]?[a-z0-9]*[@][a-z]+[.]?[a-z]*",todos_los_mails))
            Strmails_en_lista="".join(mails_en_lista)
            with open ("base_de_datos.txt","a") as arch_mail:
                    arch_mail.write (Strmails_en_lista)
                    return ("Mails copiados")
            
#[a-z0-9]+[._-]?[a-z0-9][@][a-z]+[.]?[a-z]
print (mails_secretos())
