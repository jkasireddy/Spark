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
  order by 1,2,3


