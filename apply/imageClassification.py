import cv2
import numpy as np
import os

orb = cv2.ORB_create(nfeatures= 1000)

path = 'imageQuery'
images = []
classNames = []
myList = os.listdir(path)
print(myList)

for cl in myList:
    imgCur = cv2.imread(f'{path}/{cl}', 0)
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])
    
print(classNames)

def findDes(images):
    desList = []
    for img in images:
        kp , des = orb.detectAndCompute(img, None)
        desList.append(des)
    return desList

def findId(img, desList):
    matchList = []
    kp2 , des2 = orb.detectAndCompute(img, None)
    finalValue = -1
    bf = cv2.BFMatcher()
    for des in desList:
        matches = bf.knnMatch(des, des2 ,k=2)
        good = []
        for m,n in matches:
            if m.distance < 0.75*n.distance:
                good.append([m])
        matchList.append(len(good))
    print(matchList)    

    if matchList != 0:
        finalValue = matchList.index(max(matchList))
            
    return finalValue  



dess = findDes(images)
print(len(dess))


test = cv2.imread('maybe/Resident Evil 7 Biohazard Gold Edition - PlayStation 4.jpg')

gray=cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)

gameId = findId(gray, dess)

print(gameId)

if gameId!=-1:
    cv2.putText(test, classNames[gameId], (50,50), cv2.FONT_HERSHEY_COMPLEX, 1 , (255,0,0), 2)

cv2.imshow('fianl results', cv2.resize(test, (700,700)) )

cv2.waitKey(0)
cv2.destroyAllWindows()

# img1 = cv2.imread('imageQuery/PS4 resident evil 3.jpg')
# img2 = cv2.imread('imageTrain/re3.jpg')

# orb = cv2.ORB_create(nfeatures= 1000)
# kp1 , des1 = orb.detectAndCompute(img1, None)
# kp2 , des2 = orb.detectAndCompute(img2, None)

# bf = cv2.BFMatcher()
# matches = bf.knnMatch(des1, des2 ,k=2)

# good = []
# for m, n in matches:
#     if m.distance < 0.75*n.distance:
#         good.append([m])
        
# img3= cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
# print(len(good))

# cv2.imshow('img', img3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()