
import json

filename = 'store.db'

fd_w = open(filename, 'w')
personinfos = [{'username':'monkey', 'email':'monkey@reboot.com', 'password':'123456'}]
data = json.dumps(personinfos) # dumps -> (obj -> str)
fd_w.write(data)
fd_w.close()


fd_r = open(filename, 'r')
data = fd_r.read()
obj = json.loads(data)  # loads -> (str -> obj)
new_person_info = {'username':'monkey', 'email':'monkey@reboot.com', 'password':'123456'}
obj.append(new_person_info)
fd_r.close()

#print json.dumps(obj, indent=4)

fd_w = open(filename, 'w')
fd_w.write(json.dumps(obj))
fd_w.close()



def writeFile(filename, data):
    pass
    

def readFile(filename):
    return data
