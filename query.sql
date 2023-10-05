

SELECT*
FROM budget_balance WHERE Countries = 'Turkey'

SELECT*
FROM current_account  WHERE Countries = 'Turkey'

SELECT*
FROM growth WHERE Countries = 'Turkey'

SELECT*
FROM inflation WHERE Countries = 'Turkey'

SELECT*
FROM investment WHERE Countries = 'Turkey'
--Getting data from these 5 statements 
INSERT INTO `Turkiye_forecast`(Budget_Balance,Current_Account,Economic_Growth,Inflation,Investment)
VALUES (-5.68,-3.96,2.67,45,31)
--And add the data to our table

SELECT*FROM `Turkiye_forecast`
