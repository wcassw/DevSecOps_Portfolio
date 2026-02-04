terraform {
  backend "s3" {
    bucket         = "DevSecOps-Portfolio-tfstate-bucket"
    key            = "ec2/terraform.tfstate"
    region         = "eu-west-1"
    dynamodb_table = "DevSecOps-Portfolio-tfstate-lock"
    encrypt        = true
  }
}
