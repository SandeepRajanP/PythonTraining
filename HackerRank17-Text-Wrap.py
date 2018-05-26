def wrap(string, max_width):
    a = []
    for i in range(len(string)/max_width):
        try:
            print string[i*max_width:i*max_width+max_width]
        except:
            break
    return  string[(i+1)*max_width:len(string)]
                
