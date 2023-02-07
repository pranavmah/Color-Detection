import cv2
import pandas as pd

pth = r'C:\Users\Lenovo\Downloads\stones1.jpg'
image1 = cv2.imread(pth)

#defining global variables that will be used later
clicked = False
r = g = b = x_pos = y_pos = 0

# Reading csv file using pandas
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colordetection.csv', names=index, header=0, encoding='unicode_escape')

# function to find the most similar colour and determine the minimum distance from all colours
def color_name(R, G, B):
    min = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= min:
            min = d
            c_name = csv.loc[i, "color_name"]
    return c_name


# function to obtain x,y coordinates of mouse double click
def draw_funct(event1, m, n, flag1, param):
    if event1 == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = m
        y_pos = n
        b, g, r = image1[n, m]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_funct)

while True:

    cv2.imshow("image", image1)
    if clicked:

        # cv2.rectangle(image, start point, endpoint, color, thickness)-1
        cv2.rectangle(image1, (20, 20), (750, 60), (b, g, r), -1)

        # Using a text string to display the name of a color and its RGB values
        text = color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(image1, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # The text will be displayed in black for very light colours.
        if r + g + b >= 600:
            cv2.putText(image1, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # Inorder to break the loop use the 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()