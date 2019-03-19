from faceComparator import *

f = faceComparator()
def runFaceComparator():
    while True:
        faceFound = f.faceDetection()
        if(faceFound):
            faceConfidence = f.findFace()
def checkKeyPress():
    while True:
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows() 
            f.addFace()
            f.buildRecognizer()
    
def main():
    runFaceComparator()
    checkKeyPress()

main()
        
