# import sys
import pandas as pd
import re

line = ['7\n', 'Leonardo DiCaprio,The Revenant\n', 'Christian Bale,Vice\n', 'Morgan Freeman,Shawshank Redemption\n',
        'Leonardo DiCaprio,The Great Gatsby\n', 'Christian Bale,American Psycho\n', 'Morgan Freeman,The Dark Knight\n',
        'Christian Bale,The Dark Knight\n', 'Samuel L. Jackson,Pulp Fiction']
# print(list[0])


# get number of lines to read
fline = int(line[0])
# pop the first line
lst = line.pop(0)

# Final List with number of lines to read
final_list = line[:fline]

# creating pandas dataframe
df = pd.DataFrame(final_list, columns=["column"])

# splitting DAtaframe and assigning the columns
df1 = pd.DataFrame(df.column.str.split(',', 1).tolist(),
                   columns=['ACTOR_NAME', 'MOVIE_NAME'])
# replacing the Dataframe's new line `\n`
df1 = df1.replace(r'\n', ' ', regex=True)
# creating a max_movies coulumns grouping by actor on numbef of movies acted
df1 = df1.groupby('ACTOR_NAME').count()['MOVIE_NAME'].reset_index(name="max_movies")
# Applying dense rank and applying ascending order
df1['Rank'] = df1.max_movies.rank(method='dense', ascending=False)

# creating a filder condition on rank column
filter = df1['Rank'] <= 3

# the final dataframe with only top 3 actors based on the rank
top3_df = df1.where(filter)
for x in range(0, 3):
    var = top3_df.iloc[x, 0]
    print(var)
