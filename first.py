tablica = []

while True:
    user_input = input()


    splitted_user_input = user_input.split()

    if splitted_user_input[0] in ['print','insert','remove','append','sort', 'pop', 'reverse']:
        # print("norton commander")

        if splitted_user_input[0] == "insert":
            if len(splitted_user_input) > 2:
                    place = int(splitted_user_input[1])
                    value = int(splitted_user_input[2])
                    tablica.insert(place,value)
            else:
                continue

        if len(splitted_user_input) == 2:
            eval("tablica." + splitted_user_input[0] + "(" + splitted_user_input[1] + ")")
            tablica.sort()

        if splitted_user_input[0] == 'print':
            print(tablica)

        if splitted_user_input[0] in ['sort','pop','reverse']:
            eval("tablica." + splitted_user_input[0]+"()")


    else:
        #print("##error - there is no such a command")
        pass

