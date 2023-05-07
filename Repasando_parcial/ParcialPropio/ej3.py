import re
def patron_7_54 (string):
    return re.findall ("&([^&].*?)[%][$]",string)

print (patron_7_54("vwrevwn35n32o5n32n532jin532&vewkvnemvoseomom&l;mewvemwovew;m*&^6vaevvkems;vevm%$vewwv%$ feveve vkwe[31532095llc;ac7777&&&&&f32f45123%$"))
