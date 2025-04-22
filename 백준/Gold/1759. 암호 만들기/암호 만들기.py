from itertools import combinations

vowels = {'a', 'e', 'i', 'o', 'u'}

L, C = map(int, input().split())
word = sorted(list(input().split()))

for comb in combinations(word, L):
    vowel_count = sum(1 for c in comb if c in vowels)
    consonant_count = L - vowel_count

    if vowel_count >= 1 and consonant_count >= 2:
        print(''.join(comb))