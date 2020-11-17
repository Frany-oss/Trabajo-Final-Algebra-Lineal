from matplotlib import pyplot

def extract_eq(eq_str):
    
    eq_str = eq_str.split()
    #print(eq_str)
    a = 0
    b = 0
    s = 0
    r = 0
    for i in range(len(eq_str)):
        if "x" in eq_str[i]:
            if eq_str[i]== "x":
                a = 1
            else:
                a = int(eq_str[i][0:len(eq_str[i])-1])

        if "y" in eq_str[i]:
            if eq_str[i]== "y":
                b = 1
            else:
                b = int(eq_str[i][0:len(eq_str[i])-1])

        if "<=" in eq_str[i]:
            s = 0

        if ">=" in eq_str[i]:
            s = 1

        if "<=" in eq_str[i] or ">=" in eq_str[i]:
            r = int(eq_str[i+1])
            
    print("extract: {}, {} ,{} ,{}".format(a , b , s, r))
    return a , b , s, r

def input_data():
    f_obj = []
    ineq  = []
    ineq_s = [] 
    ineq_r = []
    obj_a = int(input("Según la funcion objetivo ax+by introduce a:"))
    obj_b = int(input("Según la funcion objetivo ax+by introduce b:"))
    f_obj = [obj_a,obj_b]
    n = int(input("Cuantas inecuaciones desea ingresar [3,8]"))
    for i in range(n):
        print("Inequacion Número {}:".format(i+1))
        
        inequation = input("Ingrese inecuación: (Ej: 2x + 3y <= 4 o 10x + 2y >= 4)")
        
        a , b , s ,r = extract_eq(inequation)
        #print("Valores obtenidos:")
        #print(a,b,s,r)
        ineq.append([a,b])
        ineq_s.append(s)
        ineq_r.append(r)
        
    return f_obj , ineq , ineq_s , ineq_r

def create_label(a , b , s , r):
    print(a,b,s,r)
    ineq_label = "" 
    
    if a == 1:
        ineq_label = ineq_label + "x"
    elif a > 1:
        ineq_label = ineq_label + "{}x".format(a)
    if 0< a and 0 <b:
        ineq_label = ineq_label + " + "
    if b == 1:
        ineq_label = ineq_label + "y"
    elif b > 1: 
        ineq_label = ineq_label + "{}y".format(b)
    
    if s:
        symbol = " >= "
    else:
        symbol = " <= "
    
    ineq_label += symbol
    ineq_label += "{}".format(r)
    
        
    return ineq_label

def graph_inec(ineq,ineq_r,ineq_s):
    for i , r , s in zip(ineq,ineq_r,ineq_s):
        l=10
        #print(i,r)
        x=i[0]
        y=i[1]
        if x != 0 and y!=0:
            px= [r/x,0]
            py = [0,r/y]
        elif x!=0:
            px= [r/x,r/x]
            py = [0,l]
        elif y != 0:
            px = [0,l]
            py = [r/y,r/y]
            
        
        equation = create_label(i[0],i[1],s,r)
        
        pyplot.plot(px,py, label=equation)
    pyplot.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    
    
def intersection(L1, L2, R1, R2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = R1 * L2[1] - L1[1] * R2
    Dy = L1[0] * R2 - R1 * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False
    
def graph_inter(ineq,ineq_r):
    interX = []
    interY = []
    inter = []
    for ine1 , r1 in zip(ineq,ineq_r):
        for ine2 , r2 in zip(ineq,ineq_r):
            R = intersection(ine1,ine2,r1,r2)
            if R and R[0]>0 and R[1]>0:
                if [R[0],R[1]] not in inter:
                    interX.append(R[0])
                    interY.append(R[1])
                    inter.append([R[0],R[1]])
    for ine1 , r1 in zip(ineq,ineq_r):
#         print(ine1,r1)
        if ine1[0] != 0:
            interX.append(r1/ine1[0])
            interY.append(0)
            inter.append([r1/ine1[0],0])
        if ine1[1] != 0:
            interY.append(r1/ine1[1])
            interX.append(0)
            inter.append([0,r1/ine1[1]])
    
    interX.append(0)
    interY.append(0)
    inter.append([0,0])
    pyplot.plot(interX,interY,'ro')
    return interX,interY , inter


def comprobar_region(ineq,ineq_r,ineq_s,inter):
    interR = []
    for i in inter:
        valido = True
        for ine,r,s in zip(ineq,ineq_r,ineq_s):
            p = int((ine[0]*i[0]) + (ine[1]*i[1]))
            #print(p)
            if s == 0:
                if p <= r:
                    pass
                else:
                    print(p," ",r)
                    valido = False
            if s == 1:
                if p >=r:
                    pass
                else:
                    valido =False
                    print(p," ",r,">=")
                
        if valido:
            interR.append([int(i[0]),int(i[1])])
            #interR.append([int(i[0]),int([1])])
    
    
    return interR

def max_obj(obj,inter):
    maximo = 0
    for i in inter:
        m = obj[0]*i[0] + obj[1]*i[1]
        if m> maximo:
            maximo = m
            intersect = [i[0],i[1]]
    return maximo,intersect
def min_obj(obj,inter):
    minimo = 100000000
    for i in inter:
        m = obj[0]*i[0] + obj[1]*i[1]
        if m< minimo:
            minimo = m
            intersect = [i[0],i[1]]
    return minimo,intersect


def linearp():
    f_obj , ineq , ineq_s ,ineq_r = input_data()
    graph_inec(ineq,ineq_r,ineq_s)
    interX,interY , inter = graph_inter(ineq,ineq_r)
    inter = comprobar_region(ineq,ineq_r,ineq_s,inter)
    max_obj, max_coord = min_obj(f_obj,inter)
    min_obj, min_coord = max_obj(f_obj,inter)
    pyplot.title("Gráfica de las indecuaciones")
    print("El máximo posible es:{} , en las coordenadas {}".format(max_obj,max_coord))
    print("El mínimo posible es:{} , en las coordenadas {}".format(min_obj,min_coord))
    pyplot.show()
    return m,i
    