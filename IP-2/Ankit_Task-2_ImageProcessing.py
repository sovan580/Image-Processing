import cv2
import numpy
def A():
    print("FUNCTION A:")
    img1=cv2.imread('Image1.jpg')
    print("Image1[Rows,Columns,Channels]=",img1.shape)
    img2=cv2.imread('Image2.jpg')
    print("Image2[Rows,Columns,Channels]=",img2.shape)
A()
def B():
    print("FUNCTION B:")
    img1=cv2.imread('Image1.jpg')
    img2=cv2.imread('Image2.jpg')
    px1=img1[473,640]
    px2=img2[322,488]
    print(f"Pixels values of Image1(R,G,B):{px1[2],px1[1],px1[0]}")
    print(f"Pixels values of Image2(R,G,B):{px2[2],px2[1],px2[0]}")
B()
def C():
    print("FUNCTION C:")
    img1=cv2.imread('Image1.jpg')
    gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    ret,thresh1=cv2.threshold(gray1,185,255,0)
    contours,hierarchy=cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img1,contours,-1,(0,255,0),4)
    a=len(contours)
    for i in range(0,a):
        print(f'Area-{i}=',cv2.contourArea(contours[i]))
        print(f'Perimeter-{i}=',cv2.arcLength(contours[i],True))
    cv2.imshow('image1_ss1',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    img2=cv2.imread('Image2.jpg')
    gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret,thresh2=cv2.threshold(gray2,185,255,0)
    contours,hierarchy=cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img2,contours,-1,(0,255,0),4)
    b=len(contours)
    for j in range(0,b):
        print(f'Area-{j}=',cv2.contourArea(contours[j]))
        print(f'Perimeter-{j}=',cv2.arcLength(contours[j],True))
    cv2.imshow('image2_ss1',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
C()
def D():
    print("FUNCTION D:")
    img1=cv2.imread('Image1.jpg')
    gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    ret,thresh1=cv2.threshold(gray1,185,255,0)
    contours,hierarchy=cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    a=len(contours)
    c=list()
    for i in range(1,a):
        c.append(cv2.contourArea(contours[i]))
    e=max(c)
    print("Maximum Area_image-1=",e)
    for m in range(a-1):
        if e == c[m]:
            print("Perimeter_image-1=",cv2.arcLength(contours[m+1],True))
            cv2.drawContours(img1,contours,m+1,(0,0,255),4)
    cv2.imshow('image1_ss2',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    img2=cv2.imread('Image2.jpg')
    gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret,thresh2=cv2.threshold(gray2,185,255,0)
    contours,hierarchy=cv2.findContours(thresh2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    b=len(contours)
    g=list()
    for j in range(1,b):
        g.append(cv2.contourArea(contours[j]))
    k=max(g)
    print("Maximum Area_image-2=",k)
    for n in range(b-1):
        if k==g[n]:
            print("Perimeter_image-2=",cv2.arcLength(contours[n+1],True))
            cv2.drawContours(img2,contours,n,(0,0,255),4)
    cv2.imshow('image2_ss2',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
D()

def E():
    img1=cv2.imread('Image1.jpg')
    img2=cv2.imread('Image2.jpg')
    gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    gray2=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    cv2.imshow('img1_ss3',gray1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow('img2_ss3',gray2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
E()
def F():
    img1=cv2.imread('Image1.jpg')
    img2=cv2.imread('Image2.jpg')
    img1[:,:,0]=0
    img1[:,:,1]=0
    img2[:,:,0]=0
    img2[:,:,1]=0
    cv2.imshow('img1_ss4',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow('img2_ss4',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
F()


    


    
