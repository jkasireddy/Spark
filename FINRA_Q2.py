import findspark
findspark.init()
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()



activity_raw_data_df = spark.read.format("csv").option("header", True).load("")

activity_raw_data_df.createOrReplaceTempView("activity_raw_data")
print("activity_raw_data_df count: {}".format(activity_raw_data_df.count()))
activity_raw_data_df.show()
activity_raw_data_df.printSchema()


activity_data_df = spark.sql("""select ID
          ,START_TIME
          ,(int(split(START_TIME,":")[0])*60 + int(split(START_TIME,":")[1])) as START_TIME_SEC
          ,END_TIME
          ,(int(split(END_TIME,":")[0])*60 + int(split(END_TIME,":")[1])) as END_TIME_SEC
          from activity_raw_data""")
activity_data_df.createOrReplaceTempView("activity_data_tmp")

# converting START_TIME and END_TIME to seconds

activity_data_df.show()

# Sample Output

# +---+----------+--------------+--------+------------+
# | ID|START_TIME|START_TIME_SEC|END_TIME|END_TIME_SEC|
# +---+----------+--------------+--------+------------+
# |100|     10:00|           600|   12:00|         720|
# |100|     10:15|           615|   12:30|         750|
# |100|     12:15|           735|   12:45|         765|
# |100|     13:00|           780|   14:00|         840|
# |200|     10:15|           615|   10:30|         630|
# +---+----------+--------------+--------+------------+


activity_group_overlap_df = spark.sql("""
select c.ID, c.START_TIME, c.END_TIME, dense_rank() over(order by coalesce(c.B_ID, int(c.ID) * 2)) as GROUP_ID
from (
    select a.ID
      ,a.START_TIME
      ,a.END_TIME
      , max(b.ID) as B_ID
      from activity_data_tmp1 as a
      left join activity_data_tmp1 as b
      on (a.ID = b.ID
      and a.START_TIME_SEC <> b.START_TIME_SEC
      and a.END_TIME_SEC <> b.END_TIME_SEC
      and (a.START_TIME_SEC between b.START_TIME_SEC and b.END_TIME_SEC
      or a.END_TIME_SEC between b.START_TIME_SEC and b.END_TIME_SEC)
      )
      group by a.ID, a.START_TIME, a.END_TIME
  ) as c
  order by 1,2,3""")

print("activity group overlap count: {}".format(activity_group_overlap_df.count()))
activity_group_overlap_df.show()


# Output Sample
# activity_group_overlap_df count: 5
# +---+----------+--------+--------+
# | ID|START_TIME|END_TIME|GROUP_ID|
# +---+----------+--------+--------+
# |100|     10:00|   12:00|       1|
# |100|     10:15|   12:30|       1|
# |100|     12:15|   12:45|       1|
# |100|     13:00|   14:00|       2|
# |200|     10:15|   10:30|       3|
# +---+----------+--------+--------+