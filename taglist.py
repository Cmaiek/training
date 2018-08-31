import xml.etree.cElementTree as ET
# load and parse the file
xmlTree = ET.parse('8_2017_VAT_Output.xml')

elemList = []

for elem in xmlTree.iter():
  elemList.append(elem.tag) # indent this by tab, not two spaces as I did here

# now I remove duplicities - by convertion to set and back to list
elemList = list(set(elemList))

# Just printing out the result
print(elemList)