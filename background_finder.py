import matplotlib.pyplot as plt

img = plt.imread("pathtoimage") 
img_red = img[:,:,0] 
img_green = img[:,:,1]
img_blue = img[:,:,2]

rm = img_red.mean()
gm = img_green.mean()
bm = img_blue.mean()
cols = rm + gm + bm
sum = (rm/cols) + (gm/cols) + (bm/cols)

print("Quantity red : ",rm/cols)
print("Quantity green: ",gm/cols)
print("Quantity blue: ",bm/cols)
print("sum: ",sum)