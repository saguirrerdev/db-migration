resource "aws_ecr_repository" "ecr_api_repo" {
  name = "${var.project_name}-ecr-repo"

  tags = {
    "project": var.project_name
  }
}

resource "aws_ecr_repository" "ecr_mysql_repo" {
  name = "${var.project_name}-mysql"

  tags = {
    "project": var.project_name
  }
}