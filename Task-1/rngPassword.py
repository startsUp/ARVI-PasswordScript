import random, string
specialChars = '-|@.,?/!~#%^&*(){}[]\=*' #special chars for password
def generatePassword(lenRange, uCaseConstraint=1, lCaseConstraint=1, numConstraint=1, sCharConstraint=1):
    #if the constraints sum up to more than the allowed lower limit the lower limit is not valid
    if (uCaseConstraint + lCaseConstraint + numConstraint + sCharConstraint > lenRange[0]):
        raise ValueError('Character Constraints sum exceeds lower length limit')
    low, high = lenRange[0], lenRange[1]
    
    #generate minimal string satisfying the constraint
    reqString = (random.choices(string.ascii_uppercase, k=uCaseConstraint) 
                + random.choices(string.ascii_lowercase, k=lCaseConstraint) 
                + random.choices(string.digits, k=numConstraint) 
                + random.choices(specialChars, k=sCharConstraint)) 
    random.shuffle(reqString) #randomize order
    if (len(reqString) > lenRange[0]): return ''.join(reqString) # if reqString meets length constraint return it
    
    #if reqString does not meet the length constraint add random chars from the whole sample
    allChars = specialChars + string.ascii_uppercase + string.ascii_lowercase + string.digits
    pickMore = random.randint(low - len(reqString)+1, high - len(reqString)-1)
    password = random.choices(allChars, k=pickMore) + reqString
    random.shuffle(password)
    return ''.join(password)


print(generatePassword([10,24]))
