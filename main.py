from matplotlib import pyplot

f_obj = [2,1]
ineq = [[2,0],[3,1],[0,3],[0,1]]   
ineq_r = [20,5,8,2]

def graph_inec(ineq,ineq_r):
    for i , r in zip(ineq,ineq_r):
        l=20
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

        print(px,py)
        pyplot.plot(px,py)
        
graph_inec(ineq,ineq_r)
pyplot.show()