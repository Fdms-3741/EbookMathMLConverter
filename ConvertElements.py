from bs4 import BeautifulSoup

def ConvertMathElements(fp):
    missedCount = 0 
    
    soup = BeautifulSoup(fp,features='lxml')

    # Finds all equations
    for pElement in soup.find_all('math'):
        
        print("before:\n",pElement.prettify())
        # Change Tag name
        pElement.name = "p"
        
        # Get image name
        imgName = pElement['altimg']

        if not imgName:
            print("Warning: Missing altimg on Math element")
            missedCount += 1
            continue

        # Remove all attributes
        for i in list(pElement.attrs.keys()):
            del pElement[i]

        # Add image class
        pElement['class']='image'
        
        print("before:\n",pElement.prettify())

        # Create content
        aElement = soup.new_tag("a",id=imgName)
        aElement.append(soup.new_tag("img",alt="Equation "+imgName,src="../images/"+imgName))

        # Append content
        pElement.string = ""
        pElement.append(aElement)

        print("before:\n",pElement.prettify())
        
    return str(soup)

if __name__ == "__main__":

    import sys
    
    with open(sys.argv[1],'r') as fil:
        output = ConvertMathElements(fil)
    
    with open(sys.argv[1],'w') as fil:
        fil.write(output)
