import webbrowser
import time
import random


def Main():
    print("Welcome to Video Searcher by Horizon Tech.")
    vname = input("Please write the name of a video you want to see: ")
    print("Searching for " + vname + ", please wait.")
    time.sleep(random.randint(0, 4))
    print("Video found, enjoy!")
    time.sleep(1.5)
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


if __name__ == "__main__":
    Main()
