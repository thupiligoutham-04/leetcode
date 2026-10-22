/* Write your PL/SQL query statement below */
select u.name , b.bal balance
from users u inner join (select account, sum(amount) bal
                    from Transactions
                    group by account) b
on u.account = b.account
where b.bal > 10000;