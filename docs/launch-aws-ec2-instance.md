# Launching an Amazon AWS EC2 Instance

1. Navigate to the `AWS Management Console`.
![Alt text](images/aws-management-console.png)

2. Click on the `EC2` icon.
![Alt text](images/ec2.png)

3. Launch an EC2 instance by clicking the `Launch Instance` button.
![Alt text](images/launch.png)

4. Select the **Ubuntu Server 14.04 LTS** Free tier eligible instance.
![Alt text](images/launch-ubuntu-server.png)

5. Choose the `t1.micro` instance and click `Review and Launch`.
![Alt text](images/t1micro.png)
![Alt text](images/review-and-launch.png)

6. Click on `Edit Security Groups`.
![Alt text](images/edit-security-groups.png)

7. We will be adding several rules to our security group. Click on `Add Rule` each time you want to add
more rules to your security group. Your security group should resemble the following:
![Alt text](images/tcp-rules.png)

When done, click on `Review and Launch`.

8. **Optional**: Click on `Edit Storage`.
![Alt text](images/edit-storage.png)

Free tier instances allow up to 30GB of disk space. Increase the storage space if needed and click on `Review and Launch`.
![Alt text](images/increase-gb.png)

9. `Launch` your EC2 instance.
![Alt text](images/launch-ec2.png)

10. Create a new key pair, download it, then click `Launch Instances`.
![Alt text](images/key-pair.png)

11. You should now see a Launch Status Screen. Click on `View Instances`.
![Alt text](images/launch-status.png)

12. After several minutes, your EC2 instance should be running. You should also now see the Public DNS
for your EC2 instance.
![Alt text](images/public-dns.png)

13. Visit [Deploying to AWS](https://github.com/stormpython/insightfl#deploying-to-aws) to deploy your
web application to your EC2 instance.
