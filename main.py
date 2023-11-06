from node import * 

def main(): 

    #1 
    head = node('T', None)
    head = node('K', head)
    head = node('N', head)
    head = node('I', head)
    head = node('L', head)

    #2
    selection = head

    #3
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()

    #4
    selection.addNodeAfter('E')

    #5 
    selection = selection.getLink()

    #6 
    selection.addNodeAfter("D")

    #7
    selection= selection.getLink()

    #8
    selection.addNodeAfter('L')

    #9 
    selection= selection.getLink()

    #10 
    selection.addNodeAfter('I')

    #11
    selection= selection.getLink()

    #12 
    selection.addNodeAfter('S')

    #13 
    print("How many nodes does head contain:", node.listLength(head))
    print("How many nodes does selection contain:",node.listLength(selection))

    #14 
    tail = selection

    #15
    tail = tail.getLink()
    tail = tail.getLink()

    #16 
    print("How many nodes does tail contain?:",node.listLength(tail))
    
    #17
    selection.removeNodeAfter()
    selection.removeNodeAfter()


    #18 
    print("How many nodes does head contain:", node.listLength(head))
    print("How many nodes does selection contain:",node.listLength(selection))
    print("How many nodes does tail contain?:",node.listLength(tail))
    
    #19 
    head.removeNodeAfter()
    head.removeNodeAfter()


    #20
    tail = tail.getLink()

    #21 
    print("How many nodes does head contain:", node.listLength(head))
    print("How many nodes does selection contain:",node.listLength(selection))
    print("How many nodes does tail contain?:",node.listLength(tail))

    #22 
    print(f"Head Contains the letter:", node.listSearch(head,'K').get_data())
    print("Selection contains the letter:",node.listSearch(selection,'I').get_data())

    #23 
    copy = node.listCopywithTail(head)
    print(f"Copy[0] contains {node.listLength(copy[0])} nodes")
    print(f"Copy[1] contains {node.listLength(copy[1])} nodes")

    #24 
    print("First node in copy[0] conatins letter",node.listPosition(copy[0],1).get_data())
    print("First node in copy[1] conatins letter",node.listPosition(copy[1],1).get_data())

    #25
    i = 1

    while i <= 10:
        if (node.listPosition(head,i)!= None):
            print(f"Head Contains Position {i}")
        else:
            print(f"Head doesn't contains position {i}")
        
        i += 1

if __name__ == "__main__":
    main()