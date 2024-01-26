import cv2

harcascade = "model\haarcascade_russian_plate_number.xml"
cap = cv2.VideoCapture(0)
cap.set(3,640) #Set width
cap.set(4,480)#set height
min_area = 500
count = 0
while True: #infinite loop
    #reading frames from webcam
    success,img = cap.read()
    # creating a lincence plate classifier
    plate_Cascade = cv2.CascadeClassifier(harcascade)
    # converting the frame to greyscale for easy processing
    img_grey = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    plates = plate_Cascade.detectMultiScale(img_grey,1.1,4)
    #iterating through the detected plates
    for(x,y,w,h) in plates:
        area  = w*h
        # if area is greater than the minimun area draw a 
        # rectangle around the plate and display the 
        # text "Lincense Plate" on the top left corner pf the rectangle.
        # Also display the region of interesr(ROI) of the lincense plate.
        if area>min_area:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            # display the text "Lincense Plate" on the top left corner pf the rectangle.
            cv2.putText(img,'Lincence plate',(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255),2)
            img_roi = img[y:y+h,x:x+w]
            # display the region of interesr(ROI) of the lincense plate. 
            cv2.imshow("ROI",img_roi)

        cv2.imshow("Result",img_roi)

        # Saving the plate when 'S' key is pressed
        # Saving the plate when 'S' key is pressed
        #waitkey(1) means that the program will wait for 1 millisecond before proceeding to the next line of code.
        # and then check if the key pressed is 's'.
        # if the key pressed is 's', then the program will save the plate and display a message saying "Plate Saved".
        # and then wait for 500 milliseconds before proceeding to the next line of code.
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite("plate_" + str(count) + ".jpg",img_roi)
            cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
            cv2.putText(img,"Plate Saved",(150,265),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),2)
            cv2.imshow("Result",img)
            cv2.waitKey(3000)
            count += 1