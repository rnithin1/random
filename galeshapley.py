# Algorithm to find 0 < k <= n stable pairings:
#
# Take w_0, ..., w_k-1 ; m_0, ..., m_k-1. w_i's j'th preference
# is m_l, and m_l's (k - i - 1)th preference is w_i. l := i + j (mod k),
# i, j in [0, ..., k - 1]. Arbitrarily fill in preference remainder for
# m_i, w_i. For n - k w, m let their first preference be each other.
MALE = 0
FEMALE = 1

import copy
from itertools import permutations
from random import sample

n = 5
k = 5
 
galprefers = 0
guyprefers = 0

guys = 0
gals = 0 

engage = []
nengage = []
nnengage = []

class BipartiteDigraph: #Male, female
    def __init__(self):
        self.male = set(range(n))
        self.female = set(range(n))
        self.arcs = [[[],[]] for x in range(k)]
        i = 0
        for pairing in engage:
            for lst in [(m, f) for m, f in pairing.items()]:
                weightM = preference(MALE, lst[MALE], lst)
                weightF = preference(FEMALE, lst[FEMALE], lst)
                self.arcs[i][MALE].append((lst[MALE], lst[FEMALE], weightM + weightF))
                print(self.arcs)
            i += 1
        i = 0
        for npairing in nengage:
            for lst in [(m, f) for m, f in npairing.items()]:
                print(npairing)
                weightM = preference(MALE, lst[MALE], lst)
                weightF = preference(FEMALE, lst[FEMALE], lst)
                self.arcs[i][FEMALE].append((lst[MALE], lst[FEMALE], -(weightM + weightF)))
            i += 1
        print(self.arcs[0])

def preference(val, person, pairing): #If passed a female, 4, and she is paired with x, then return preference of x in 4's. (FEMALE, 4, (2,4))
    if val == FEMALE:
        return galprefers[person].index(pairing[MALE]) + 1
    else:
        return guyprefers[person].index(pairing[FEMALE]) + 1

def assign_preferences():
    global galprefers, guyprefers
    assert k <= n, "k > n"

    gal_numbers = list(range(0, k))
    gal_preference = [[0] * k for x in range(0,k)]
    guy_numbers = list(range(0, k))
    guy_preference = [[0] * k for x in range(0,k)]

    for j in range(k):
        for i in range(k):
            l = (i + j) % k
            gal_preference[i][j] = l
            guy_preference[l][k - j - 1] = i

    for i in range(k):
        gal_preference[i].extend(list(sample(range(k, n), n - k)))
        guy_preference[i].extend(list(sample(range(k, n), n - k)))

    galprefers = dict(zip(gal_numbers, gal_preference))
    guyprefers = dict(zip(guy_numbers, guy_preference))

    for i in range(k, n):
        galprefers.update({i : [i] + sample(range(0, i), i) + sample(range(i + 1, n), n - i - 1)})
        guyprefers.update({i : [i] + sample(range(0, i), i) + sample(range(i + 1, n), n - i - 1)})

    print(galprefers)
    print(guyprefers)

def check(engaged):
    inverseengaged = dict((v,k) for k,v in engaged.items())
    for she, he in engaged.items():
        shelikes = galprefers[she]
        shelikesbetter = shelikes[:shelikes.index(he)]
        helikes = guyprefers[he]
        helikesbetter = helikes[:helikes.index(she)]
        for guy in shelikesbetter:
            guysgirl = inverseengaged[guy]
            guylikes = guyprefers[guy]
            if guylikes.index(guysgirl) > guylikes.index(she):
                return False
        for gal in helikesbetter:
            girlsguy = engaged[gal]
            gallikes = galprefers[gal]
            if gallikes.index(girlsguy) > gallikes.index(he):
                return False
    return True
 
def matchmaker():
    guysfree = guys[:]
    engaged  = {}
    guyprefers2 = copy.deepcopy(guyprefers)
    galprefers2 = copy.deepcopy(galprefers)
    while guysfree:
        guy = guysfree.pop(0)
        guyslist = guyprefers2[guy]
        gal = guyslist.pop(0)
        fiance = engaged.get(gal)
        if not fiance:
            engaged[gal] = guy
            #print("  %s and %s" % (guy, gal))
        else:
            galslist = galprefers2[gal]
            if galslist.index(fiance) > galslist.index(guy):
                # She prefers new guy
                engaged[gal] = guy
                #print("  %s dumped %s for %s" % (gal, fiance, guy))
                if guyprefers2[fiance]:
                    guysfree.append(fiance)
            else:
                # She is faithful to old fiance
                if guyslist:
                    # Look again
                    guysfree.append(guy)
    return engaged

def tma():
    global guys, gals
    guys = sorted(guyprefers.keys())
    gals = sorted(galprefers.keys())
    return matchmaker()

def femaleoptimal():
    global guys, gals
    gals = sorted(guyprefers.keys())
    guys = sorted(galprefers.keys())
    return matchmaker()

def make_matches():
    for i in permutations(range(n)):
        tempdict = dict(zip(range(n), i))
        engage.append(tempdict) if(check(tempdict)) else nengage.append(tempdict)

    print(engage)
    for i in engage:
        lst = [(k, v) for k, v in i.items()]
        #if (0,0) is lst, then add (1,0), (2,0), etc. to nnengage. Do this for all
        print(lst)

def make_linear():
    for pairing in engage:
        2
 
assign_preferences()
print('\nTMA engagements:')
engaged = tma()
print(engaged)
print("hasdf")
make_matches()
#bd = BipartiteDigraph()

