# binary file to copy one image into another.
# Enet_Ip.png ---copy---> picel.png
with open('C:\\Users\\Lenovo\\Desktop\\Enet_Ip.png', 'r+b') as f:
    temp = f.readlines()
    with open('C:\\Users\\Lenovo\\Desktop\\picel.png','w+b') as f1:
        f1.writelines(temp)
        f1.seek(0)
        print(f1.read())
