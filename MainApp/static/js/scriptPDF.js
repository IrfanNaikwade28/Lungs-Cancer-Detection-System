document.body.addEventListener("onload",getPDF());
function getPDF(){
    dw = confirm("Do you Want download this pdf");
    if(dw==true){
        window.print();
    }
}