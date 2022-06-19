if __name__ == '__main__':
    N = int(input())
    list1  = []
    for _ in range(N):
        info = input().split()    #list1.command(arguements) "("+ ",".join(args) +")"
        command = info[0]
        arguments = info[1:]
        if command != "print":
            arguments = "("+ ",".join(arguments) +")"
            stmt = command+arguments
            eval("list1."+stmt)
        else:
            print(list1)