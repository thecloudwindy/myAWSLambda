# Get latest AMI ID for Amazon Linux2 OS in US
data "aws_ami" "amzlinux-us" {
  most_recent = true
  owners      = ["amazon"]
  provider = aws.usa
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-gp2"]
  }
  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  filter {
    name   = "architecture"
    values = ["x86_64"]
  }
}

# Get latest AMI ID for Amazon Linux2 OS in Tokyo
data "aws_ami" "amzlinux-tokyo" {
  most_recent = true
  owners      = ["amazon"]
  provider = aws.tokyo
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-gp2"]
  }
  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  filter {
    name   = "architecture"
    values = ["x86_64"]
  }
}

# Get latest AMI ID for Amazon Linux2 OS in Hongkong
data "aws_ami" "amzlinux-seoul" {
  most_recent = true
  owners      = ["amazon"]
  provider = aws.seoul
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-gp2"]
  }
  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }
  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  filter {
    name   = "architecture"
    values = ["x86_64"]
  }
}
