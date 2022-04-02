def preordernext(p):
    if(p.left() is not None):
        return p.left()
    elif(p.right() is not None):
        return p.right()
    else:
        node = p
        while(node.parent() is not None):
            par = node.parent()
            if(par.left() is node):
                if(par.right() is not None):
                    return par.right()
            node = par
        return None
        
def inordernext(p):
    if(p.right() is not None):
        node = p.right()
        while(node.left() is not None):
            node = node.left()
        return node
    else:
        node = p
        while(node.parent() is not None):
            par = node.parent()
            if(par.left() is node):
                return par
            node = par 
        return None

def postordernext(p):
    if(p.parent() is None):
        return None
    elif(p.parent().right() is p or p.parent().right() is None):
        return p.parent()
    else:
        node = p.parent().right()
        while(node.left() is not None):
            node = node.left()
        return node