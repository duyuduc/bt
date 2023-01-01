# Xây dựng phương thức tính A(n,x): với n và x là tham số truyền vào, phương thức có giá trị trả về là A =(x2 +x+ 1)^n + (x2-x+1)^n
def tinh_A(n,x):
    so_hang_1=int(1)
    so_hang_2=int(1)
    bt1=x**2+x+1
    bt2=x**2-x+1
    i=int(0)
    while i<n:
        so_hang_1*=bt1
        so_hang_2*=bt2
        i+=1
x=int(input(' Nhập giá trị x ='))
n=int(input(' Nhập giá trị n ='))
print("A = (x^2+x-1)^n + (x^2-x+1)^n =%d"%tinh_A(n,x))    
