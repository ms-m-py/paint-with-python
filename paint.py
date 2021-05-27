import cv2
draw=False
a=(0,0)
img_name=input("your image path to draw: ")
img=cv2.imread(img_name)
color=(0,0,0)
def on_click(event, x, y, p1, p2):
	global draw
	global img
	if event == cv2.EVENT_LBUTTONDOWN:
		draw=True
	elif event==cv2.EVENT_MOUSEMOVE:
		if draw==True:
			img=cv2.circle(img,(x,y),3,color,thickness=-1)
			# img=cv2.rectangle(img,(x-1,y-1),(x+1,y+1),color,-1)
	elif event == cv2.EVENT_LBUTTONUP:
		draw=False
cv2.namedWindow('image',cv2.WINDOW_GUI_NORMAL)
cv2.imshow("image", img)
cv2.setMouseCallback('image', on_click)
while 1:
	cv2.imshow("image",img)
	key=cv2.waitKey(60)
	if key==ord("q"):
		exit(0)
	if key==ord("r"):
		color=(0,0,250)
	if key==ord("b"):
		color=(250,0,0)
	if key==ord("g"):
		color=(0,250,0)
	if key==ord("d"):
		color=(0,0,0)
	if key==ord("w"):
		color=(250,250,250)
