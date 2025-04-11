# Proyecto Bonus #3 – Motivador Emocional Interactivo
# Autor: Luis Sosa


def verificar_estado():
    def mensaje_final(funcion):
        def envoltura():
            
            while True:
                print("---ESTADOS EMOCIONALES---")
                print("Enfocado")
                print("Dudando")
                print("Cansado")
                print("Victorioso")
                print("Salir\n")
            
                estado_emocional = input("Diga su estado emocional actual:\n").lower()
            
                if estado_emocional == "enfocado":
                    print("Estas enfocado como un caballo de carrera por llegar a la meta.")
                elif estado_emocional == "dudando":
                    print("Dudando pero sin perder el enfoque y el motivo de seguir.")
                elif estado_emocional == "cansado":
                    print("Descansa campeon y vuelve con mas hambre de llegar a donde tu quieres.")
                elif estado_emocional == "victorioso":
                    print("Con la victoria en la mano hasta el final")
                elif estado_emocional == "salir":
                    break
                else:
                    print("Aunque te equivoques seguimos luchando como guerreros. Aquí te espero de nuevo.")
                funcion()
        return envoltura
    return mensaje_final

@verificar_estado()
def emocion():
    print("\nAquí seguimos dando todo por el todo.")
    
emocion()