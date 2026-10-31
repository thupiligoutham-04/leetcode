/* Write your PL/SQL query statement below */
select d.name as "Department", e.name "Employee", salary "Salary"
from employee e , department d
where e.departmentid = d.id and 
    (e.departmentid, salary) in (select departmentid, max(salary)
                                    from employee
                                    group by departmentid);