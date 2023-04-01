from Crypto.Util.number import getPrime, isPrime, long_to_bytes
import itertools
import math
import string
import primefac

"""
Exemple 1 :
gluttony = 185434206102556811966811890443002021527
greed = 330198947881436365929375619478923955191
lust = 61230179756293686065154808886520002396606659113361047727557251510319365396657
anger = 3152348539223521494617962521296135062312694321378580820382287068537312914285
envy = 7826498250125459025707643530255856387568160343953821291217338802986547294213
clear = 97445911022346347328493862808916930868
bytes_to_long(pride.encode()) = 97445911022346347328493862808916930868
b'IOfYDLHiZlWr2E14'

prime_factors = [ 2, 2, 3, 5, 11, 157, 181, 181, 557, 8377, 292319, 4394400917, 42686709580633, 590554796504957999894305383576439559 ]
"""

"""
Exemple 2 :
anger = 53669793913171408732196856528742384141562153068446118765052227063373349441805
envy = 54195268562551666854582277080820475168115232074416582313302921028869342214929
vainglory? 

prime_factors = [ 2, 2, 2, 2, 3, 3, 2_9, 31, 71, 71, 89, 2437, 49875181, 905936487457, 9425132741803, 58924214417773777974784486741974049 ]

> Gl3LEpGNmsBbhL9E
"""

#====================================
# Récupération des infos fournies
#====================================
# Message chiffré
C = anger = int(input("anger ? > ").strip())

# Exposant de déchiffrement
d = envy = int(input("envy ? > ").strip())

# Exposant de chiffrement
e = sloth = 65537



#====================================
# Décomposition en facteurs premiers
#====================================
d_e_moins_1 = (d*e) - 1
prime_factors = list(primefac.primefac(d_e_moins_1))
print(f"{prime_factors = }")



#====================================
# Identification des combinaison de facteurs premiers éligibles
#====================================
# 1. Détermination de toutes les combinaisons possibles 
def define_combinations(elements:[], combination_size:int) -> ():
    return set(itertools.combinations(elements, combination_size))

def define_all_combinations(elements:[]) -> ():
    all_combinations = set()
    for combination_size in range(2, len(prime_factors)-1):
        combinations = define_combinations(elements, combination_size)
        all_combinations |= combinations
    return all_combinations

all_combinations_of_prime_factors = define_all_combinations(prime_factors)


# 2. Parmi toutes les combinaisons possibles, on ne retient que celles 
#    pour lesquelles, le produit + 1 donne un nombre premier de 128 bits
max_prime = 2**129
min_prime = 2**127

list_of_prime_factors_p = set()
for factors in all_combinations_of_prime_factors:
    possible_p = math.prod(factors) + 1
    if isPrime(possible_p):
        if min_prime < possible_p < max_prime:
            list_of_prime_factors_p.add(factors)


# 3. On écarte les combinaisons trop grandes 
taille_min_prime_factors_p = min(len(prime_factors_p) for prime_factors_p in list_of_prime_factors_p)
taille_max_prime_factors_p = len(prime_factors) - taille_min_prime_factors_p

list_of_prime_factors_p = set(factors for factors in list_of_prime_factors_p if taille_min_prime_factors_p<=len(factors)<=taille_max_prime_factors_p) 



#====================================
# Identification des modules de chiffrement éligibles
#====================================
modules = []
for factors_p in list_of_prime_factors_p:
    # 1. On détermine les facteurs restant (i.e. prime_factors - factors_p)
    factors_p_complement = prime_factors[:]
    for factor in factors_p:
        factors_p_complement.remove(factor)
    
    # 2. On cherche les facteurs_q complémentaires
    for factors_q in list_of_prime_factors_p:
        # On regarde si tous les facteurs de q sont dans les facteurs restants
        is_candidate = True
        for factor in factors_q:
            if not factor in factors_p_complement:
                # si NON, alors les facteurs de p et q se recoupent => ils ne peuvent pas être associés
                is_candidate = False
                break
        if is_candidate:
            # Si OUI, alors les facteurs p et q sont disjoints => ils peuvent être associés
            p = math.prod(factors_p) + 1
            q = math.prod(factors_q) + 1
            n = p*q
            modules.append(n)

#====================================
# Déchiffrement
#====================================
# Caractères autorisés pour le message en clair : alphanumériques
accepted_car_code = [ord(c) for c in string.ascii_letters + string.digits]

for n in modules:
    M = pow(C, d, n)
    M = long_to_bytes(M)
    if all(car in accepted_car_code for car in M):
        # On ne retient que les Messages en clair contenant des caractères autorisés
        print(f"possible vainglory : {M.decode()}")

