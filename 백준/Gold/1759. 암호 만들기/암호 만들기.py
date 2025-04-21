from itertools import combinations

L, C = map(int, input().split())
letters = sorted(input().split())

vowels = {'a', 'e', 'i', 'o', 'u'}

for comb in combinations(letters, L):
    volwel_count = sum(1 for c in comb if c in vowels)
    consonant_count = L - volwel_count

    if volwel_count >= 1 and consonant_count >= 2:
        print(''.join(comb))