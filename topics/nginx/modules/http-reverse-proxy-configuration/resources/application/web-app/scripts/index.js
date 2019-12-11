function updateDate() {
	var xmlHttp = new XMLHttpRequest()
	xmlHttp.open("GET", "/api/date", false)
	xmlHttp.send(null)
	document.getElementById('date').innerHTML =	xmlHttp.responseText
}
