resource "aws_ecs_cluster" "db_migration_api_cluster" {
  name = "${var.project_name}-api"
}

module "api_service" {
  source = "./api_service"
}