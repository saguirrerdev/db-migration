# db-migration API

This project involves the development of an API designed to facilitate database migration by enabling efficient batch processing. It provides the means to seamlessly transfer data from csv files to a redshift serverless warehouse.

Also provides some analiticals as
1. Amount of employees hired by department and job divided by quarter
2. List of departments where the amount of hires are over the mean for all departments

You can access to the API by this link [Migration API](http://db-migration-lb1-700957538.us-east-1.elb.amazonaws.com/)
**Note: Service is down, make a request to my email to turn on the services**

### Tool stack
* Fast API
* Docker
* ECR
* ECS
* IAM
* Secret Manager
* AWS Load Balancing
* MySQL
* Terraform
* SQL
* Store procedures
* Python