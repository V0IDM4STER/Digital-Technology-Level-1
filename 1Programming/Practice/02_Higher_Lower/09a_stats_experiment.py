# HL Component 9a - get the game stats to display nicely

game_stats = [3, 1, 6, 3, 4]

# print game outcomes
print("*** Score For Each Round ***")
list_count = 1
for item in game_stats:
    print("Round {}: {}".format(list_count, item))
    list_count += 1

# Calculate statistics
game_stats.sort()
best = game_stats[0]
worst = game_stats[-1]
average = sum(game_stats)/len(game_stats)

print()
print("*** Summary Statistics ***")
print("Best: {}".format(best))
print("Worst: {}".format(worst))
print("Average: {:.2f}".format(average))