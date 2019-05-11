def namelist(names):
    nnm = ''
    if not names:
        return nnm
    else:
        if len(names) == 1:
            return names[0]['name']
        elif len(names) == 2:
            return names[0]['name']+" & "+names[1]['name']
        else:
            for nn in range(0, len(names)-2):
                nnm += names[nn]['name']+", "
            return nnm+names[-2]['name']+" & "+names[-1]['name']

#https://www.codewars.com/kata/53368a47e38700bd8300030d