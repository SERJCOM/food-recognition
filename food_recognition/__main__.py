import sys
from recognition import FoodRecognition

def print_food_name(img_path):
    model = FoodRecognition()
    print(model.eval(img_path)[0])

def arg_handler():

    if sys.argv[1] == "help":
        print("usage: food_recognition IMAGE_PATH")
    
    else:
       print_food_name(sys.argv[1])



def main():
    if(len(sys.argv)) == 1:
        print_food_name("assets/images/bread5.jpg")

    else:
        arg_handler()
    

if __name__ == "__main__":
    main()