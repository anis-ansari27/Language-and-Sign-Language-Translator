from django.shortcuts import render
from django.http import HttpResponse
from translate import Translator
import pyttsx3

      
# Create your views here.
list_lan = ['English','Spanish','Hindi','French','Tamil','German','Bengali','Chinese','Arabic','Greek','Gujarati',
                        'Italian','Korean','Malayalam','Marathi','Punjabi','Russian','Telugu']
def SpeakText(command,var):  
    engine = pyttsx3.init() 
    engine.setProperty("language",var)
    engine.say(command) 
    engine.runAndWait() 

def text(request):
    
    source_text = request.GET.get('src','')
    result = ""
    lang_src = "English"
    lang_dest = "English"
    lang_src = request.GET.get('src-language','')
    lang_dest = request.GET.get('dest-language','')
    translator = Translator(from_lang=lang_src, to_lang=lang_dest)
    result = translator.translate(source_text)
    SpeakText(result,lang_src)
    return render(request,"home/text.html",{
        "src-combo": lang_src,
        "dest-combo": lang_dest,
        "languages": list_lan,
        "result": result,
        "source_text":source_text,
    })

def sign(request):

    isl_gif=['hello','fine','bored','good night','i don\'t know','please','rofl','safe']
        
    arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
        's','t','u','v','w','x','y','z']

    sign_text = request.GET.get('sign-source','')
    copy_st = sign_text
    sign_text = sign_text.lower()
    newc = ''
    for loop in sign_text:
        if loop.isalpha() or loop==' ':
            newc+=loop
    sign_text = newc
    collage = []
    if(sign_text in isl_gif):
        collage.append("/static/home/Gifs/"+sign_text+".gif")
    else:
        for i in range(len(sign_text)):
            if(sign_text[i] in arr):                      
                ImageAddress = '/static/home/alphabets/'+sign_text[i]+'.jpg'
                collage.append(ImageAddress)  
            elif(sign_text[i]==' '):
                ImageAddress = '/static/home/alphabets/space.jpg'
                collage.append(ImageAddress)                    
            else:
                continue
   
    
    return render(request, "home/sign.html",{
        "signtext": copy_st,
        "collage": collage,
    })
    


