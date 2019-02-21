var listaElementos = document.getElementsByClassName("anchor-link");
while (listaElementos.length > 0) {
	listaElementos[0].parentNode.removeChild(listaElementos[0]);
}