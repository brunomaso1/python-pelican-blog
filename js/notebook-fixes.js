/**
 * Elimina todos los elementos que contienen la clase "anchor-link". Estos elementos se dan debido a que pelican
 * genera una P en cada titulo. El objetivo es eliminar dicha P que tiene asociada dicha clase.
 **/
function fixAnchorLinks(){
	var listaElementos = document.getElementsByClassName("anchor-link");
	while (listaElementos.length > 0) {
		listaElementos[0].parentNode.removeChild(listaElementos[0]);
	}
};

/**
 * Cambia el título de la TOC por uno más chico, ya que el que genera pelican es muy grande.
 **/
function cambiarTituloTOC(){
	h1Element = document.getElementsByClassName("tocSkip")[0].parentNode;
	pElement = h1Element.nextSibling;
	pElement.innerText = "Tabla de contenido:";
	h1Element.remove();
};

/**
 * Elimina todos los promtps generados por pelican.
 **/
function deleteNotebookPrompts(){
	// Promts de entrada.
	var listaElementos = document.getElementsByClassName("prompt input_prompt");
	while (listaElementos.length > 0) {
		listaElementos[0].parentNode.removeChild(listaElementos[0]);
	}
	
	// Promts de salida.
	var listaElementos = document.getElementsByClassName("prompt output_prompt");
	while (listaElementos.length > 0) {
		listaElementos[0].parentNode.removeChild(listaElementos[0]);
	}
	
	// Promts en general.
	var listaElementos = document.getElementsByClassName("prompt");
	while (listaElementos.length > 0) {
		listaElementos[0].parentNode.removeChild(listaElementos[0]);
	}
};

fixAnchorLinks();
cambiarTituloTOC();
deleteNotebookPrompts();