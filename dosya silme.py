from pathlib import Path
import shutil
import os

klasor=r'C:\Users\USER\Desktop\b'  # Silinecek dosyaların ana konumu



sayac=0
for yol in Path(klasor).rglob('*.pdf'): #  " ........ "uzantılı Dosyları klasörler içinde arama 
  
   
    os.remove(yol)                        # dosya silme
    

    son3=str(yol)[-2:]
   
    sayac+=1
   
    print(yol) 
    
print("Toplam Taranan Dosya sayısı : ",sayac)    

    
    
        
    
    
    


    

 

    
