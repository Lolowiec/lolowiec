class HttpRequest:
    def __init__(self, req: str): 
        reqlines = req.splitlines()                      
        firstrow =  reqlines[0].split(' ')              
        self.headers = {}
        self.method = firstrow[0]
        self.path = firstrow[1]
        self.verson = firstrow[2]
        self.body = ''
        if '\n\n' in req:
            P = req.find('\n\n')
            self.body = req[P+2:]
        for i in range(1, len(reqlines)) :
            headerrow = reqlines[i]                     
            B = headerrow.find(':')
            key = headerrow[:B]
            value = headerrow[B+1:]
            self.headers[key] = value.strip()