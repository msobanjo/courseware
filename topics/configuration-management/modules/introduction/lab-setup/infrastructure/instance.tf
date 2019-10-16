resource "aws_instance" "portal" {
  # ubuntu 18.04
  count = 3
  ami = "ami-0c30afcb7ab02233d"
  instance_type = "t2.micro"
  subnet_id = "${aws_subnet.default.id}"
  vpc_security_group_ids = ["${aws_security_group.default.id}"]
  associate_public_ip_address = true
  key_name = "default-key-pair"
  provisioner "local-exec" {
    command = "ansible-playbook -i '${self.public_ip},' --ssh-common-args=\"-o 'StrictHostKeyChecking=no'\" --private-key ~/.ssh/lab_id_rsa -u ubuntu lab-setup/configuration/playbook.yml"
  }
}

resource "aws_instance" "service" {
  # ubuntu 18.04
  count = 2
  ami = "ami-0c30afcb7ab02233d"
  instance_type = "t2.micro"
  subnet_id = "${aws_subnet.default.id}"
  vpc_security_group_ids = ["${aws_security_group.default.id}"]
  associate_public_ip_address = true
  key_name = "default-key-pair"
}

resource "aws_instance" "nginx_service" {
  # ubuntu 18.04
  ami = "ami-0c30afcb7ab02233d"
  instance_type = "t2.micro"
  subnet_id = "${aws_subnet.default.id}"
  vpc_security_group_ids = ["${aws_security_group.default.id}"]
  associate_public_ip_address = true
  key_name = "default-key-pair"
}

resource "aws_instance" "nginx_portal" {
  # ubuntu 18.04
  ami = "ami-0c30afcb7ab02233d"
  instance_type = "t2.micro"
  subnet_id = "${aws_subnet.default.id}"
  vpc_security_group_ids = ["${aws_security_group.default.id}"]
  associate_public_ip_address = true
  key_name = "default-key-pair"
}

