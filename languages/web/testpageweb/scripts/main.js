const miTitulo = document.querySelector("h1");
miTitulo.textContent = "¡Hola mundo!";

miTitulo.onclick = function () {
	alert("¡Ouch! ¡Deja de pincharme!");
};

console.log("jajaja");

let miImage = document.querySelector("img");
miImage.onclick = function () {
	let miSrc = miImage.getAttribute("src");

	if (miSrc === "images/firefox-logo.svg") {
		miImage.setAttribute("src", "images/firefox2.png");
	} else {
		miImage.setAttribute("src", "images/firefox-logo.svg");
	}
};

let miButton = document.querySelector("button");

if (!localStorage.getItem("nombre")) {
	estableceNombreUsuario();
} else {
	let nombreAlmacenado = localStorage.getItem("nombre");
	miTitulo.textContent = "Mozilla es genial, " + nombreAlmacenado;
}

function estableceNombreUsuario() {
	let miNombre = prompt("Por favor, ingresa tu nombre.");

	if (!miNombre) {
		estableceNombreUsuario();
	} else {
		localStorage.setItem("nombre", miNombre);

		miTitulo.textContent = "Mozilla es genial, " + miNombre;
	}
}
