import math
def g1(x):
    b=math.exp((16388.684*(x**2)-11560.48*(x**3))/2477.572)
    return b
def g1_x(x):
    b=g1(x)*(16388.684*2*(x)-11560.48*3*(x**2))/2477.572
    return b
def g2_x(x):
    b=g2(x)*(((-952.036)*2*(x)+11560.48*3*(x**2))/2477.572)
    return b
def g2(x):
    b=math.exp(((-952.036)*(x**2)+11560.48*(x**3))/2477.572)
    return b
def u(x,y):
    b=x*g1(1-x)-y*g1(1-y)
    return b
def v(x,y):
    b=(1-x)*g2(x)-(1-y)*g2(y)
    return b
def u_x(x,y):
    b=g1(1-x)-x*g1_x(1-x)
    return b
def u_y(x,y):
    b=y*g1_x(1-y)-g1(1-y)
    return b
def v_x(x,y):
    b=(1-x)*g2_x(x)-g2(x)
    return b
def v_y(x,y):
    b=g2(y)-(1-y)*g2_x(y)
    return b
def J(x,y):
    b=u_x(x,y)*v_y(x,y)-v_x(x,y)*u_y(x,y)
    return b
xi=1 #Inital guess for x and y
yi=0
x=0
i=0
while (i<100):
    x=xi-(u(xi,yi)*v_y(xi,yi)-v(xi,yi)*u_y(xi,yi))/J(xi,yi)
    y=yi-(v(xi,yi)*u_x(xi,yi)-v_x(xi,yi)*u(xi,yi))/J(xi,yi)
    i=i+1
    ep1=abs((x-xi)/x)
    ep2=abs((y-yi)/y)
    
    if(ep1<0.00001 and ep2<0.00001):
        print(x," ",y," ",u(x,y)," ",v(x,y))
        break
    xi=x
    yi=y
