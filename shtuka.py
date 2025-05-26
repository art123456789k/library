def shtuka():
    
    for i in range(1,10):
        d = f''
        for t in range(1,10):
            if i == 1:
                if len(str(t*i)) < 2:
                    d += f' {t*i}   '
                else:
                    d += f' {t*i}  '
            else:
                if len(str(t*i)) < 2:
                
                    d += f' {t*i}  |'
                else:
                    d += f' {t*i} |'
        d += f'\n    ------------------------------------------'       
        print(d)
    
            
shtuka()