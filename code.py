import cv2

clusters = [[],[],[],[],[],[],[],[],[],[]]

for i in range(10):
    path = r'C:\Users\Naeem\Desktop\Jahanzeb\DIP\DIP Lab\Project 2\number\c' + str(i) + '.jpg'
    template = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    clusters[i].append(template)

i = 11
for j in range(10):
    for k in range(4):
        path = r'C:\Users\Naeem\Desktop\Jahanzeb\DIP\DIP Lab\Project 2\number\t' + str(i+k) + '.jpg'
        sample = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        clusters[j].append(sample)
    i += 4
    if i == 51:
        break


test = cv2.imread(r'C:\Users\Naeem\Desktop\Jahanzeb\DIP\DIP Lab\Project 2\number\test.jpg', cv2.IMREAD_GRAYSCALE)

distance = 10000000
closest = 0

for i in range (10):
    for j in range(len(clusters[i])):
        dist = clusters[i][j] - test
        temp = list(map(sum, dist))
        total = sum(temp)

        if total < distance:
            distance = total
            closest = i

print('Cluster assigned to test image: ', closest)

cv2.waitKey(0)
cv2.destroyAllWindows()
