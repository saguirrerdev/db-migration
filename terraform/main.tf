resource "aws_ecr_repository" "ecr_repo" {
  name = "${var.project}-ecr-repo"

  tags = {
    "project": var.project
  }
}