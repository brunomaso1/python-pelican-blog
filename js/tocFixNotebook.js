h1Element = document.getElementsByClassName("tocSkip")[0].parentNode;
pElement = h1Element.nextSibling;
pElement.innerText = "Tabla de contenido:";
h1Element.remove();