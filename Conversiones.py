while True:
    print(f"Primera version")
    print(f"Segunda version")
   print(f"Selecciona una opcion:")
   print(f"1. Convertir de kilometros a millas")
   print(f"2. Convertir de kilogramos a libras")
   print(f"3. Convertir de grados Celsius a Fahrenheit")
   print(f"4. Salir")
   opcion=int(input("Indique una opcion:"))
   if (opcion<0 or opcion>4):
       print(f"Indica una opcion valida, gracias")
   if opcion==4:
        print(f"¡Hasta luego!")
        break
   elif opcion==1:
       #while True:
           v1=input("Ingresa los kilometros que desea convertir a millas:")
           v1f=float(v1);
           if v1f<=0:
              print(f"Ingresa valores validos, gracias")
           
           if v1f>0:
              conversion=v1f*0.621371
              print(f"{v1f} kilometros son {conversion} millas")
           #break
   elif opcion==2:
        #while True:
           v2=input("Ingrese los kilogramos que desea convertir a libras:")
           v2f=float(v2);
           if v2f<=0:
              print(f"Ingrese valores validos, gracias")
                
           if v2f>0:
              conversion=v2f*2.20462
              print(f"{v2f} kilogramos son {conversion} libras")
           #break
        
   elif opcion==3:
       #while True:
           v3=input("Ingrese los °C que desea convertir a °F:")
           v3f=float(v3);
           if v3f<=0:
               print(f"Ingrse valores validos, gracias")
               
           if v3f>0:
               conversion=v3f*1.8+32
               print(f"{v3f} °C son {conversion} °F")

   resp = input("\n¿Quieres hacer otra conversión? (s/n): ").strip().lower()
   if resp != "s":
        print("Gracias por usar el conversor. ¡Hasta luego!")
        break
    
    
    
    
       
       
       
  
       
       