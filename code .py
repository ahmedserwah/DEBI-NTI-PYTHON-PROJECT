def ps(a):
    try:
        import re
        PATTERN = re.compile(r'^([a-z]+?)\1*$')
        seg = PATTERN.findall(a)[0]
        return seg, len(a) / len(seg)   
    except:
        print('PLEASE TRY AGAIN ')
############################################################################
def is_palindrome(s):
    try:
        s=s.lower()
        txt=s
        txtS=txt[::-1]
        if txt == txtS:
            return  True
        else:
            return  False
    except:
        print('trY again(:')

############################################################################
def solve(a,b):
    import re
    try:
     return bool (re.fullmatch(a.replace("*",".*"),b))
    except:
        print('trY again')
############################################################################
def find_nth_occurrence(sub_string, string, occ=1):
    try:
        place = string.find(sub_string,0,len(string))
        if occ==1:
            return place
        else:
            while occ >1:
                place = string.find(sub_string,place+1,len(string))
                occ-=1
                print(place)
        return place
    except:
        print('try again')
            
        
