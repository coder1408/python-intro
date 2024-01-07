import sys

def main():
    while True:
        sys.stdout.write("🍫 ")
        sys.stdout.flush()
        user_input = input()
        if user_input == "":
            break

if __name__ == "__main__":
    main()







