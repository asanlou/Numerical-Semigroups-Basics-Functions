def Comprobacioninicial(x,A):
    if x == 0:
        return True
    if x < 0:
        return False    
    if x < min(A):
        return False
    for i in A: 
        if i == 1:
            return True
    return elSolitario(x,A)
  
  def elSolitario(x,A):
    for i in A:
        if x % i == 0:
            return True
    return porParejas(x,A)
  
def porParejas(x,A):
    for a in A:
        for b in A:
            if a != b:
                for j in range(1,int(x)): # acotar el range
                    i = 1 
                    while a*j + i*b <= x:
                        i = i+1
                        if x == a*j + i*b:
                            return True
    return 0
  
  def menageaTrois(x,A):
    for a in A:
        for b in A:
            if a == b:
                break
            for c in A:
                if a == c or b == c:
                    break  
                for j in range(1,int(x)): # acotar el range
                    i = 1 # HAY QUE REINICIAR EL j EN ALGUN MOMENTO????
                    for k in range(1,int(x)): # acotar el range
                        while a*j + b*k + i*c < x:
                            i = i+1
                            if x == a*j + b*k + i*c:
                                return True
     return False
      
      def Pertenece(x,A):
    return Comprobacioninicial(x,A)
