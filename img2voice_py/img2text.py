import cv2
import pytesseract


#def img2text()


if __name__ == "__main__":

    # load image
    img = cv2.imread("image/ocr_test.png")
    # gray scale converting
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # tesseract instance created
    # text file extracting
    text = pytesseract.image_to_string(gray_img)
    # printing text file
    print(text)

    text_file = open("img2text.txt", "w")
    text_file.write(text)

    text_file.close()