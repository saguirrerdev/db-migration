output "api_repository_url" {
  value = aws_ecr_repository.ecr_api_repo.repository_url
}

output "mysql_repository_url" {
  value = aws_ecr_repository.ecr_mysql_repo.repository_url
}