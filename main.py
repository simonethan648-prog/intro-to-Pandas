import pandas as pd
print('---PART 1: Pandas Series ---')
scores = [98500, 87200, 76400, 65100, 54800]
players = pd.Series(scores, index=['Nightwolf', 'StarBlaze', 'PixelKing', 'CyberFox', 'IronStorm'])
print(players)

print()
print('--- PART 2: Pandas DataFrame ---')
data = {
    'Player': ['Nightwolf', 'StarBlaze', 'PixelKing', 'CyberFox', 'IronStorm'],
    'Level': [42, 38, 35, 30, 27],
    'Score': [98500, 87200, 76400, 65100, 54800],
    'Wins': [210, 185, 162, 140, 118]
}
df = pd.DataFrame(data)
print(df)

print()
print('--- PART 3: Accessing Rows ---')
print('Row 0 (top player):')
print(df.loc[0])
print()
print('Rows 2 and 3:')
print(df.loc[2:3])

print()
print('--- PART 4: Reading a CSV File ---')
full_df = pd.read_csv('leaderboard.csv')
print('First 5 rows (head):')
print(full_df.head())
print()
print('Last 3 rows (tail):')
print(full_df.tail(3))
print()
print('Dataset info')
print(full_df.info())

print()
print('--- PART 5: Cleaning Data ---')
print()

print()
print()
print()

print()