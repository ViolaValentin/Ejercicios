import os,sys,re,glob

def buscar_mails (Carpeta_con_archivos,carpeta_salida, archivo_salida):
    #creo carpeta
    #pongo archivos adentro
    #traigo archivos
    #leo archivos y guardo en variable
    #busco patron de mail
    #creo carpeta
    #creo archivo de salida con mails adentro

    os.mkdir (Carpeta_con_archivos)
    os.chdir (Carpeta_con_archivos)
    string1="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean blandit diam erat, ut fermentum ante imperdiet id. Quisque vestibulum egestas porttitor. Suspendisse volutpat felis et nisl pulvinar, at efficitur urna sollicitudin. In vel tellus consequat, dignissim ex in, hendrerit massa. Vivamus lobortis velit et lorem pellentesque, nec bibendum elit lobortis. Pellentesque luctus risus blandit ornare pretium. In dapibus urna nec consequat auctor. Etiam vel neque semper, dictum quam et, hendrerit orci. Etiam consectetur faucibus lacus dictum cursus. Phasellus non volutpat arcu.
Mauris in sapien sit amet mi pulvinar viverra. Etiam nisi felis, maximus ut nibh a, egestas lacinia ipsum. Fusce id mattis nulla. Nam finibus, mi sit amet rutrum luctus, libero nisl bibendum tortor, ac malesuada tortor odio eu felis. Sed lacinia nulla eu sem cursus consectetur. In fringilla hendrerit arcu vel faucibus. Integer quis gravida orci, vel imperdiet lacus. Mauris lacinia lacus nec tempor suscipit. Fusce sit amet nibh pellentesque, dapibus sapien vel, dapibus magna
Fusce placerat dapibus sollicitudin. Phasellus viverra, diam vitae porta posuere, lacus nunc consequat ante, non auctor mauris tortor at nunc. Quisque ultrices, enim varius mattis tristique, magna leo pulvinar nisl, sit amet sollicitudin sapien orci lobortis leo. Nam pharetra@yahoo.com arcu ipsum, at laoreet libero ornare vel. Donec eget rhoncus urna. Ut faucibus nibh urna, eu lacinia nisi malesuada malesuada. Sed libero justo, dignissim eu placerat imperdiet, ultricies sed orci. Donec elementum purus id mi tristique viverra. Nunc vitae magna pretium, suscipit nisl non, porttitor libero. Suspendisse erat@hotmail.com justo, tristique et blandit et, lacinia ut enim. Integer volutpat euismod faucibus. Quisque rhoncus ante tellus, ac tristique velit sodales eget. Morbi maximus malesuada nulla elementum cursus. Vestibulum volutpat urna nunc, ut laoreet quam iaculis a.
Aliquam tincidunt, odio eget auctor congue, nunc leo aliquet urna, nec ultrices elit dui et enim. Phasellus convallis at libero id eleifend. Maecenas sagittis finibus sagittis. Sed leo eros, convallis vulputate augue accumsan, convallis auctor ligula. Morbi sapien odio, rhoncus nec gravida nec, sollicitudin ac nunc. Integer hendrerit vel risus et fringilla. Nam consequat velit id ex accumsan, eget finibus@gmail.com tellus elementum. Nullam bibendum, ipsum non vestibulum consequat, eros odio elementum dui, in mattis magna leo a ex. In rutrum lorem vel risus malesuada, ut rutrum felis venenatis. Nullam lobortis turpis ligula, vitae fringilla purus suscipit ullamcorper. Integer felis risus, ornare sed maximus ut, dictum ac nisl. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tellus magna, rhoncus@cielo.com in porttitor eu, hendrerit at massa. Curabitur enim erat, posuere ac sagittis eget, luctus at risus. Etiam mollis ut augue a feugiat. Quisque et lacinia felis.
Donec sit amet sollicitudin tellus. In pellentesque nulla justo, vel scelerisque dui ullamcorper sit amet. Donec condimentum pharetra nunc, non egestas mi dignissim et. Donec bibendum mi non justo posuere tempor. Nam tempor ex non hendrerit hendrerit. Donec pretium eros non tortor sagittis, viverra auctor tellus vehicula. Sed pharetra ullamcorper magna, in porttitor turpis. Nullam condimentum finibus diam, sed ornare augue. Duis sollicitudin nulla et nulla fermentum, in elementum@yahoo.com odio semper. Mauris consectetur neque non dictum commodo. Suspendisse tincidunt orci@gmail.com nisl, et tincidunt neque blandit sed. Vestibulum in ligula leo. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec lobortis iaculis urna, et ornare lorem fermentum at. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
Sed tincidunt, felis a efficitur facilisis, mi augue sollicitudin sapien, at lobortis elit purus ut augue. Donec et diam nec arcu pellentesque lobortis non id sapien. Proin nec massa sit amet eros porttitor rutrum fringilla nec tellus. Donec imperdiet, lorem ac tristique finibus, erat metus dictum lectus, in venenatis libero dolor id lorem. Pellentesque venenatis sodales tellus eget consectetur. Nulla rutrum est ut imperdiet tristique. Donec vestibulum urna semper consectetur ultricies. Proin vitae eros elementum, vehicula nisi ac, bibendum quam. Duis gravida consectetur tellus, in lobortis dui faucibus eu. Donec lacus ipsum, tristique sit amet egestas vitae, aliquam non tortor. Etiam et fringilla quam, nec facilisis ipsum.
Maecenas facilisis mattis urna, sit amet pretium orci accumsan eget. Sed sit amet nibh sit amet tortor ornare faucibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Fusce eleifend, ante vitae placerat cursus, nibh orci lacinia est, ut scelerisque tellus odio nec leo. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus sit amet iaculis justo. Sed id ex porta, ultricies orci vitae, tempor nibh. Etiam dapibus ex non massa mollis ultrices. Nam ut ante ligula. In pellentesque diam porta, luctus eros in, ultrices purus. Donec eu dapibus elit. Proin id augue ut elit pellentesque tincidunt vel a ligula."""
    string2="""What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
Why do we use it It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
Where does it come from Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham. You can contact H. Rackham in HRackham@gmail.com or Rackham@yahoo.com.ar
Where can I get som There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc."""
    text1= open ("archivo1.txt","a").write(string1)
    text2= open ("archivo2.txt","a").write (string1)

    txt=glob.glob("*.txt")
    ambos_archivos_leidos=[]
    for archivos_leidos in txt:
        with open (archivos_leidos,"r") as leer_arch:
            ambos_archivos_leidos.append(leer_arch.read())
    ambos_archivos_leidosStr="".join(ambos_archivos_leidos)
    todos_los_mails=re.findall ("[a-z0-9]+[._-]?[a-z0-9]*[@][a-z]+[.]?[a-z]*",ambos_archivos_leidosStr)

    todos_los_mailsStr="\n".join(todos_los_mails)

    os.mkdir (carpeta_salida)
    os.chdir (carpeta_salida)
    with open (archivo_salida, "a") as arch_salida:
        arch_salida.write (f"{todos_los_mailsStr}")

buscar_mails ("./carpeta_con_mails","./carpeta_salida","salida.txt")