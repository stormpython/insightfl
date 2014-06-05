# Creating an Amazon AWS RDS MySQL Database

1. Sign in to your [Amazon AWS](http://aws.amazon.com/) account.
2. From the *Console Home*, click on the `RDS` icon.
![Alt text](images/rds.png)

3. Click on `Launch a DB Instance`.
![Alt text](images/launch-db-instance.png)

4. Select `MySQL Community Edition`.
![Alt text](images/select-mysql.png)

5. Select `No` regarding the production question and click `Next`.
![Alt text](images/no-production.png)

6. Specify the DB details. **Be sure to select a `db.t1.micro` instance and select `No` for the Multi-AZ Deployment
option.** You can allocate up to *30GB* of storage. Fill in an identifier, username, and password, then click `Next`.
![Alt text](images/db-details.png)

7. Add a `Database Name` in the Configure Advanced Settings step. Then click `Launch DB Instance`.
![Alt text](images/db-name.png)

8. Click on `View your DB instances on the DB Instances page`.
![Alt text](images/view-db.png)

9. After several minutes, your RDS database should be created. You should now have an RDS Endpoint.
![Alt text](images/mysql-db-instance.png)

To connect to your RDS database, open the terminal and type:

    ```
    mysql -h myinstance.123456789012.us-east-1.rds.amazonaws.com -P 3306 -u mymasteruser -p
    ```

10. Congratulations! You have launched your RDS database.
