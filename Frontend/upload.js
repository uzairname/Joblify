var pdfDropArea = document.getElementById("pdf-drop-area");
var pdfFileInput = document.getElementById("pdf-file");

pdfDropArea.ondragover = function() {
    this.className = "hover";
    return false;
}

pdfDropArea.ondragleave = function() {
    this.className = "";
    return false;
}

pdfDropArea.ondrop = function(e) {
    e.preventDefault();
    this.className = "";
    pdfFileInput.files = e.dataTransfer.files;
    displayPDF();
}

pdfFileInput.onchange = function() {
    displayPDF();
}

function displayPDF() {
    var pdfFile = pdfFileInput.files[0];
    var pdfUrl = URL.createObjectURL(pdfFile);
    var pdfDisplay = document.getElementById("pdf-display");
    pdfDisplay.innerHTML = "<embed src='" + pdfUrl + "' width='100%' height='600px'/>";
}