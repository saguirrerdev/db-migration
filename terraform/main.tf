module "ecr" {
  source = "./ecr"

  project_name = var.project_name
}

module "ecs" {
  source = "./ecs"

  project_name = var.project_name
}

module "network" {
  source = "./network"

  project_name = var.project_name
}