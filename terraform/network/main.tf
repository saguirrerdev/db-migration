resource "aws_lb" "api_lb" {
  name = "${var.project_name}-lb1"
}