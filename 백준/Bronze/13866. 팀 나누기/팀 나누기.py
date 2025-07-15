import sys
input = sys.stdin.readline

skill_levels = list(map(int, input().split()))
skill_levels.sort()
team1 = skill_levels[0] + skill_levels[-1]
team2 = skill_levels[1] + skill_levels[2]
print(abs(team1 - team2))
