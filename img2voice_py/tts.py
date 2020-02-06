import pyttsx3

if __name__ == "__main__":

    # load text file to string type
    textfile = open("img2text.txt", "r")
    # put string type in function
    engine = pyttsx3.init()


    for line in textfile:
        if line == "\n":
            continue

        engine.say(line)
        engine.runAndWait()

    print("Done")