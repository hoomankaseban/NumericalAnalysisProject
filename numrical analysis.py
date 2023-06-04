import numpy as np
import scipy as sip 
#ساخت تابع دلتا2 از طریق فرمول دلتا
def F(fx):
    delta=[]
    for i in range(len(fx)-2):
        delta_i=fx[i]+fx[i+2]-(2*fx[i+1])
        delta.append(delta_i)
    return delta
#تابع سازنده وارون ماتریس
def compute_inverse(A):
    try:
        inverse_A = np.linalg.inv(A)
        return inverse_A
    except np.linalg.LinAlgError:
        print("Error: The matrix is not invertible.")
        return None
#حل کننده معادله جواب شیب ها
def solve_equation(A, B):
    X = A * B
    return X

points={-2:2,-1:1,0:0,1:1,2:2}# the x and y points of function
x=list(points.keys())
fx=list(points.values())
num_of_points=5 #تعداد نقاط مثالتان را وارد کنید
num_of_func=num_of_points-1 #تعداد ضابطه اسپلاین
num_of_coef_func=num_of_func-1 #تعداد شیب های مجهول --- شیب های اندیس صفر و ان ام برابر صفر است

#Create Matrix A based on Natural Qubic Splayn Formula
A=np.zeros((num_of_coef_func,num_of_coef_func))
for i in range(num_of_coef_func):
    if(i!=0):
            A[i][i-1]=1
    A[i][i]=4
    if(i!=num_of_coef_func-1):
            A[i][i+1]=1
#print(A)
#ساخت ماتریس دلتا
delta2=F(fx)
#print(delta2[1])

#A*coef=delta2>>>>>coef=A^-1 * delta2
#محاسبه وارون آ
A_inverse=compute_inverse(A)

M=[]
M.append(0)
#محاسبه شیب ها
coef=solve_equation(A_inverse,delta2)   #coef=A^-1 * delta2
for i in range (len(coef)):
    M.append(coef[i][1])
M.append(0)
#print(M)
# M matrix have all coeffs

#Calculate h
h=1#متساوی الفاصله
d=[]
c=[]
for i in range(len(x)-1):
    d.append(fx[i]-M[i])
    c_formula=((fx[i+1]-fx[i])/h)+h*(M[i]-M[i+1])
    c.append(c_formula)
#print(d)
#print(c)
S=[]
        