# SAMPLE DATA in CSV FILE AS
# GAME                COMPLETION_TIME   TIMEPAYOUT_RATE
# Pac-man             75                250
# Speed Racer         45                280
# Pump it Up          30                150
# Space Invaders      35                120
# Mario Bros          30                200
# Mortal Kombat       15                100
# Atari Breakout      60                300
# Super Tetris        90                350
# Star Wars           20                110
# Street Fighter II   10                90


# Answer
"""
 The code is written in jupyter notebook as a pyspark, PANDAS and PYTHON2 coding functionality from local setup
 """

import findspark
findspark.init()
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()




game_data_df = spark.read.format("csv").option("header", True).load("/Users/apple/Desktop/Projects/Spark/game_data.csv")

game_data_df.createOrReplaceTempView("game_data_tmp")

bestie_ordered_df= spark.sql("""
    select  GAME,
        cast(COMPLETION_TIME as BIGINT) as  COMPLETION_TIME,
        PAYOUT_RATE,
            round((PAYOUT_RATE/COMPLETION_TIME), 2) as BEST_PAYOUT_RATE
    from game_data_tmp 
        order by 4x desc,    
                2 asc      
                """).show()
row_count = bestie_ordered_df.count()

# Output
# game_data_df count: 10
# +-----------------+---------------+-----------+-------------------+
# |             GAME|COMPLETION_TIME|PAYOUT_RATE|PAYOUT_RATE_PER_MIN|
# +-----------------+---------------+-----------+-------------------+
# |Street Fighter II|             10|       90.0|                9.0|
# |    Mortal Kombat|             15|      100.0|               6.67|
# |       Mario Bros|             30|      200.0|               6.67|
# |      Speed Racer|             45|      280.0|               6.22|
# |        Star Wars|             20|      110.0|                5.5|
# |       Pump it Up|             30|      150.0|                5.0|
# |   Atari Breakout|             60|      300.0|                5.0|
# |     Super Tetris|             90|      350.0|               3.89|
# |   Space Invaders|             35|      120.0|               3.43|
# |          Pac-man|             75|      250.0|               3.33|
# +-----------------+---------------+-----------+-------------------+

"""
converting spark dataframe to Pandas Dataframe
"""

import pandas as pd
pandas_df = bestie_ordered_df.toPandas()

def best_games_for_adam_to_play(row_count):
    total = 0
    game_list= []
    for x in range(0,row_count):
        sum_value = pandas_df.get_value(x,'COMPLETION_TIME')
        games = pandas_df.get_value(x,'GAME')
        game_list.append(games)
        total += sum_value
        if total == 120:
            print total
            print game_list
            break
        else:
            continue

"""
OUTPUT
120
[u'Street Fighter II',u'Mortal Kombat',u'Mario Bros',u'Speed Racer',u'Star Wars']
"""
# TODO
# if total time is <120 and adding a next COMPLETION_TIME value is greater than 120 then
# look for the difference and see if the remaining values in the list matches that value and get the game of it or get the
# next lesser value of the difference

# Note: The above TODO code is not covered here
