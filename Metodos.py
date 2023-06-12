class Metodos:
    def ingreso_datos(self,List,tam):
        i=0
        while(i<tam):
            print("ingrese un valor en la List[",i,"]")
            num=int(input("numero "))
            List.append(num)
            i=i+1
    def imprimir_valores(self,List, tam):
        for i in range(tam):
            print(List[i])