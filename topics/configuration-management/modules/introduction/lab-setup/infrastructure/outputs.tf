output "portal_public_ips" {
    value = "${aws_instance.portal.*.public_ip}"
}
output "portal_private_ips" {
    value = "${aws_instance.portal.*.private_ip}"
}
output "service_public_ips" {
    value = "${aws_instance.service.*.public_ip}"
}
output "service_private_ips" {
    value = "${aws_instance.service.*.private_ip}"
}
output "nginx_portal_public_ip" {
    value = "${aws_instance.nginx_portal.public_ip}"
}
output "nginx_service_private_ip" {
    value = "${aws_instance.nginx_service.private_ip}"
}
output "nginx_service_public_ip" {
    value = "${aws_instance.nginx_service.public_ip}"
}
