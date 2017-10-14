import dc3

myDc3 = dc3.Dc3()

def processAndShow(content):

    procesed1 = myDc3.process(content)
    
    print ("------ Procesado ------")
    print (content)
    print ("-----------------------")
    for i, idx in enumerate(myDc3.indexes):
        print ("{}) {}".format(i, content[idx:]))

content = "yabbadabbado"

processAndShow(content)
processAndShow(content[0:-3])
processAndShow(content[-3:])