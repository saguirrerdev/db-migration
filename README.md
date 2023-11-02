# db-migration API

This project involves the development of an API designed to facilitate database migration by enabling efficient batch processing. It provides the means to seamlessly transfer data from csv files to a redshift serverless warehouse.

Also provides analiticals over the data as
1. Amount of employes hired by department and job divided by quarter
2. List of departments where the amount of hires are over the mean for all departments

### Tool stack
* Fast API
* Docker
* ECR
* ECS
* S3
* IAM
* Secret Manager
* AWS Load Balancing
* Redshift
* Terraform
* SQL
* Store procedures