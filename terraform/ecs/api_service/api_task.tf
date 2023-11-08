data "aws_iam_role" "ecsTaskExecutionRole" {
  name = "ecsTaskExecutionRole"
}
resource "aws_ecs_task_definition" "fast_api" {
  family                = "fast-api-app"
  container_definitions = <<TASK_DEFINITION
  [
        {
            "name": "fast-api",
            "image": "423396695262.dkr.ecr.us-east-1.amazonaws.com/db-migration-ecr-repo:latest",
            "cpu": 0,
            "portMappings": [
                {
                    "name": "fast-api-8000-tcp",
                    "containerPort": 8000,
                    "hostPort": 8000,
                    "protocol": "tcp",
                    "appProtocol": "http"
                }
            ],
            "essential": true,
            "environment": [],
            "environmentFiles": [],
            "mountPoints": [],
            "volumesFrom": [],
            "ulimits": [],
            "logConfiguration": {
                "logDriver": "awslogs",
                "options": {
                    "awslogs-create-group": "true",
                    "awslogs-group": "/ecs/",
                    "awslogs-region": "us-east-1",
                    "awslogs-stream-prefix": "ecs"
                },
                "secretOptions": []
            }
        }
    ]
  TASK_DEFINITION

  task_role_arn      = data.aws_iam_role.ecsTaskExecutionRole.arn
  execution_role_arn = data.aws_iam_role.ecsTaskExecutionRole.arn

  network_mode = "awsvpc"

  cpu    = 512
  memory = 1024

  requires_compatibilities = [
    "FARGATE"
  ]

  runtime_platform {
    cpu_architecture        = "X86_64"
    operating_system_family = "LINUX"
  }
}