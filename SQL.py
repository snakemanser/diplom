# SELECT c.login,
#        Count(o.indelivery)
# FROM   "Coiruers" AS c
#        INNER JOIN "Orders" AS o
#                ON c.id = o.courier_id
# WHERE  o.indelivery = true
# GROUP  BY c.login



# SELECT track,
#        CASE
#          WHEN indelivery = true THEN "1"
#          WHEN cancelled = true THEN "-1"
#          WHEN finished = true THEN "2"
#          ELSE "0"
#        END AS status
# FROM   "Orders"