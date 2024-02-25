passing_attempts = float(input())
completions = float(input())
passing_yards = float(input())
touchdown_passes = float(input())
interceptions = float(input())

a = ((completions / passing_attempts) - 0.3) * 5
b = ((passing_yards / passing_attempts) - 3) * 0.25
c = (touchdown_passes / passing_attempts) * 20
d = 2.375 - ((interceptions / passing_attempts) * 25)
if a < 0:
    a = 0
else:
    a = a

if b < 0:
    b = 0
else:
    b = b

if c < 0:
    c = 0
else:
    c = c

if d < 0:
    d = 0
else:
    d = d

if a > 2.375:
    a = 2.375
else:
    a = a

if b > 2.375:
    b = 2.375
else:
    b = b

if c > 2.375:
    c = 2.375
else:
    c = c
if d > 2.375:
    d = 2.375
else:
    d = d

print(((a + b + c + d) / 6) * 100)
