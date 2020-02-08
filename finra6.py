# import sys
import pandas as pd
import re
import itertools


line = ['6\n', 'Pac-man,80,400\n', 'Mortal Kombat,10,30\n', 'Super Tetris,25,100\n', 'Pump it Up,10,40\n',
        'Street Fighter II,90,450\n', 'Speed Racer,10,40']
# print(list[0])


# get number of lines to read
fline = int(line[0])
# pop the first line
lst = line.pop(0)

# Final List with number of lines to read
final_list = line[:fline]

print(final_list)

# creating pandas dataframe
df = pd.DataFrame(final_list, columns=["column"])

# splitting DAtaframe and assigning the columns
df1 = pd.DataFrame(df.column.str.split(',', 2).tolist(),
                   columns=['GAME', "COMPLETION_TIME","PAYOUT_RATE"])
# replacing the Dataframe's new line `\n`
df1 = df1.replace(r'\n', '', regex=True)


df1['PAYOUT_RATE_PER_MIN'] = df1.apply(lambda row: int(row.PAYOUT_RATE) / int(row.COMPLETION_TIME), axis = 1)
ordered_df=df1.sort_values([ 'COMPLETION_TIME','PAYOUT_RATE_PER_MIN'], ascending=[False,False])
print(ordered_df)
total = 0
game_timings= []
for x in range(0,fline):
    var1 = ordered_df.iloc[x, 1]
    var2 = ordered_df.iloc[x, 0]
    game_timings.append((int(var1),var2))
print(game_timings)
a=[i[0] for i in game_timings]

# numbers = [1, 2, 3, 7, 7, 9, 10]

game_combinations = [seq for i in range(len(a), 0, -1) for seq in itertools.combinations(a, i) if sum(seq) == 120]
print(game_combinations)
# for x in range(0,6):
#     sum_value = int(ordered_df.get_value(x,'COMPLETION_TIME'))
#     games = ordered_df.get_value(x,'GAME')
#     game_list.append(games)
    # total += sum_value
    # if total == 120:
    #     print(total)
    #     print(game_list)
    #     break
    # else:
    #     continue
#
# creating a max_movies coulumns grouping by actor on number of movies acted
# df1 = df1.groupby('ACTOR_NAME').count()['MOVIE_NAME'].reset_index(name="max_movies")
# Applying dense rank and applying ascending order
# df1['Rank'] = df1.max_movies.rank(method='dense', ascending=False)

# creating a filder condition on rank column
# filter = df1['Rank'] <= 3

# the final dataframe with only top 3 actors based on the rank
# top3_df = df1.where(filter)
# for x in range(0, 3):
#     var = top3_df.iloc[x, 0]
#     print(var)
