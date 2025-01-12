resource "aws_instance" "instance-in-us" {
  ami           = data.aws_ami.amzlinux-us.id
  instance_type = var.ec2_instance_type
  provider      = aws.usa
  vpc_security_group_ids = [aws_security_group.allow_tls.id]
}

resource "aws_instance" "instance-in-seoul" {
  ami           = data.aws_ami.amzlinux-seoul.id
  instance_type = var.ec2_instance_type
  provider      = aws.seoul
}

resource "aws_instance" "instance-in-tokyo" {
  ami           = data.aws_ami.amzlinux-tokyo.id
  instance_type = var.ec2_instance_type
  provider      = aws.tokyo
}
