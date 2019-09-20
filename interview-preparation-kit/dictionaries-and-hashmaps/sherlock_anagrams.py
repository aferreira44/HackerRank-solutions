import pytest
import time

t0 = time.time()

def frequency(s):
    f = {}
    for c in s:
        f[c] = f[c] + 1 if c in f else 1
    return f

def sherlockAndAnagrams(s):
    count = 0
    inc = 1
    pairs = [] # Guarda os índíces iniciais das substrings que formam anagramas

    # incrementa tamanho da string que será comparada
    while(inc <= len(s)-1):

        i = 0

        # Itera para obter as substrings base para comparação
        while (i <= len(s)-inc-1):

            base = s[i:i+inc]

            # print('base', base, i, i+inc)
            # print('freq_base', freq_base)

            j = 1

            # Itera para obter as substrings que serão comparadas com a base
            while(j <= len(s)-1):
                # Compara somente anagramas que já não foram comparados com substrings anteriores
                if [[j], [i]] not in pairs:
                    # Compara somente as substrings do mesmo tamanho da base e não compare com ele mesmo
                    if (j <= len(s)-inc and (i != j and i+inc != j+inc)):
                        freq_base = frequency(base)
                        compare = s[j:j+inc]
                        freq_compare = frequency(compare)

                        # print('compare', compare, j, j+inc)
                        # print('freq_compare', freq_compare)

                        isAnagram = True

                        # Itera 
                        for key in freq_base:
                            try:
                                if (freq_base[key] != freq_compare[key]):
                                    isAnagram = False
                                    break
                            except KeyError:
                                isAnagram = False
                                break

                        if isAnagram:
                            # print('base', base, i, i+inc)
                            # print('compare', compare, j, j+inc)

                            pairs.append([[i], [j]])
                            count += 1
                            # print("\ncount" + str(count) + "\n")
                
                j += 1
            i += 1        
        inc += 1

    return count

sherlockAndAnagrams('abba')


# def sherlockAndAnagrams(s):
#     inc = count = 0
#     i = 0
#     pair = { 'base': [0, 1], 'compare': [1, 2] }

#     # Loop each increment
#     while inc < len(s)-1:
#         # Set base
#         base = s[pair['base'][0]:pair['base'][1]]

#         while i <= len(s):
#             compare = s[pair['compare'][0]:pair['compare'][1]]

#             print(base, compare)

#             pair['compare'][0] += 1
#             pair['compare'][1] += 1

#             i += 1

#         pair['base'][0] += 1
#         pair['base'][1] += 1

#         inc += 1
    
#     return count

def test_0():
    assert sherlockAndAnagrams('abba') == 4
    assert sherlockAndAnagrams('abcd') == 0

def test_1():
    assert sherlockAndAnagrams('ifailuhkqq') == 3
    assert sherlockAndAnagrams('kkkk') == 10

def test_2():
    assert sherlockAndAnagrams('ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel') == 399
    assert sherlockAndAnagrams('gffryqktmwocejbxfidpjfgrrkpowoxwggxaknmltjcpazgtnakcfcogzatyskqjyorcftwxjrtgayvllutrjxpbzggjxbmxpnde') == 471
    assert sherlockAndAnagrams('mqmtjwxaaaxklheghvqcyhaaegtlyntxmoluqlzvuzgkwhkkfpwarkckansgabfclzgnumdrojexnrdunivxqjzfbzsodycnsnmw') == 370
    assert sherlockAndAnagrams('ofeqjnqnxwidhbuxxhfwargwkikjqwyghpsygjxyrarcoacwnhxyqlrviikfuiuotifznqmzpjrxycnqktkryutpqvbgbgthfges') == 403
    assert sherlockAndAnagrams('zjekimenscyiamnwlpxytkndjsygifmqlqibxxqlauxamfviftquntvkwppxrzuncyenacfivtigvfsadtlytzymuwvpntngkyhw') == 428

def test_6():
    assert sherlockAndAnagrams('cdcd') == 5