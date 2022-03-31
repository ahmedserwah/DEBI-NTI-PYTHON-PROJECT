def ps(a):
    try:
        import re
        PATTERN = re.compile(r'^([a-z]+?)\1*$')
        seg = PATTERN.findall(a)[0]
        return seg, len(a) / len(seg)   
    except:
        print('PLEASE TRY AGAIN ')

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


def solve(a,b):
    import re
    try:
     return bool (re.fullmatch(a.replace("*",".*"),b))
    except:
        print('trY again(:')

            
        
