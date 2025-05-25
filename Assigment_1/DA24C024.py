import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

columnames=['x','y']
img=pd.read_csv('C:/Users/Mansha/Desktop/Default Dataset (1).csv', names=columnames, header=None)
print("Glimpse of Dataset",img.head())
print(img)
print("Plot of original image:")
img.plot('x','y', kind='scatter', figsize=(4,5),color='black')
plt.show()

#_______________DATA CLEANING/PREPARATION________________________

#Rounding coordinate points to one decimal place
img=img.round(1)
#removing faulty values (if any)
img=img[img['y']>=0]
img=img[img['x']>=0]

#_______________CONVERTING TO A SPARSE MATRIX________________________

img_matrix=np.zeros((1000,1000))
#Updating values to 1 wherever a datapoint exists
for ind in img.index:
    [i,j]=[img['x'][ind], img['y'][ind]]
    r,c=int(i*10),int(j*10)
    img_matrix[r,c]=1       

#____________________________ROTATING THE IMAGE BY 90 DEGRESS_____________________________
#We do so by transposing and then multiplying it by an antidiagonal matrix

rm=img_matrix
rm=np.transpose(rm) #Transposing

#CREATING ANTIDIAGONAL MATRIX
antidiag=np.zeros((1000,1000))
for i in range(1000):
    antidiag[i,-i-1]=1

#MULTIPLYING TO ROTATE
multi=np.matmul(rm,antidiag)
print(multi)

#CONVERTING THE ROTATED SPARSE MATRIX TO X-Y COORDINATES FOR PLOTTING
imrot=[]
for i in range(1000):
    for j in range(1000):
        if multi[i,j]==1:
            r,c=i/10,j/10
            imrot.append([r,c])

#CONVERTING BACK TO DATAFRAME
imrot=pd.DataFrame(imrot)
imrot.rename(columns={0:'x_rot',1:'y_rot'},inplace=True)

#VISUALIZINF THE ROTATED IMAGE MATRIX
imrot.plot('x_rot','y_rot', kind='scatter', figsize=(5,4),color='black')
plt.show()

#______________________FLIPPING___________________________
#In flipping vertically, the y coordinate gets reflected to the negative y axis while the x remains the same

imflip=[]
flip_mat=[]

for i in range(1000):
    for j in range(1000):
        if img_matrix[i,j]==1:
            y=100-j #flipping
            r,c=i/10,y/10
            imflip.append([r,c])
imflip=pd.DataFrame(imflip)
imflip.rename(columns={0:'xflip',1:'yflip'},inplace=True)
imflip.plot('xflip','yflip', kind='scatter', figsize=(4,5),color='black')
plt.show()


#APART FROM THESE INBUILT FUNCTIONS LIKE np.rot90 AND np.flip can also be used