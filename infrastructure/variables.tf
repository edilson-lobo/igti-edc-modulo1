variable "aws_region" {
  default = "us-east-2"
}

variable "lambda_function_name" {
  default = "IGTIexecutaEMR"
}

variable "key_pair_name" {
  default = "elobo-igti-teste"
}

variable "airflow_subnet_id" {
  default = "subnet-06f8d51532672a2d9"
}

variable "vpc_id" {
  default = "vpc-06872304132e932f7"
}