CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  declare x int;
  set x = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT distinct salary FROM Employee order by salary desc limit x, 1
  );
END
