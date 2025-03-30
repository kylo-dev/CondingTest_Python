import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  all_voice = list(input().split())
  animal = []

  while True:
    say = input().rstrip()
    if say == "what does the fox say?":
      break

    ani, goes, voice = say.split()
    animal.append(voice)

  all_voice = [voice for voice in all_voice if voice not in animal]

  print(" ".join(all_voice))
