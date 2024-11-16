def count_words(file_name):
    path = 'Python Crash Course/Capitulo_10/'
    try:
        with open(path+file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + file_name + " doest not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + file_name + " has about " +
              str(num_words) + " words.")


file_name = 'alice.txt'
count_words(file_name)
