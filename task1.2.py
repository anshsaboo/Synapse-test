gadgets = [
    ("Explosive Batarangs", 3, True),
    ("Batarangs", 5 , True),
    ("Smoke Pellets", 0, False),
    ("Tear Gas Grenades", 2, True),
    ("Night Vision Goggles", 1, True),
    ("Batclaw", 0, False),
    ("Grapple Gun", 3, True),
    ("Batsignal", 0, False),
    ("Utility Belt",1,True),
    ("Batmobile Tires",4,True)
        ]


def SortKey(gadget):
    gname, gcount, gflag = gadget
    gflag=True
    return ( gflag, -gcount, gname)


gsorted = sorted(gadgets, key=SortKey)


for gadget in gsorted:
    print(gadget)


    '''
    commented output
('Batarangs', 5, True)
('Batmobile Tires', 4, True)
('Explosive Batarangs', 3, True)
('Grapple Gun', 3, True)
('Tear Gas Grenades', 2, True)
('Night Vision Goggles', 1, True)
('Utility Belt', 1, True)
('Batclaw', 0, False)
('Batsignal', 0, False)
('Smoke Pellets', 0, False)

    '''