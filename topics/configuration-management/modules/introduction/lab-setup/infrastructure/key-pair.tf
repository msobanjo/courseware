resource "aws_key_pair" "default" {
  key_name = "default-key-pair"
  public_key = "${file("~/.ssh/lab_id_rsa.pub")}"
}
