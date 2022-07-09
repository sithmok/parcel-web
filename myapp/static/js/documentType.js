

// function yesnoCheck(that) {
//     if (that.value == "ปกติ") {

//         let doc2 = document.getElementsByName("document2");
//         let doc3 = document.getElementsByName("document3");
//         let doc4 = document.getElementsByName("document4");

//         doc2.removeAttribute('required');
//         doc3.removeAttribute('required');
//         doc4.removeAttribute('required');

//         document.getElementById("document1").style.display = "block";
//         document.getElementById("document2").style.display = "none";
//         document.getElementById("document3").style.display = "none";
//         document.getElementById("document4").style.display = "none";

//     } else {
//         document.getElementById("document1").style.display = "block";
//         document.getElementById("document2").style.display = "block";
//         document.getElementById("document3").style.display = "block";
//         document.getElementById("document4").style.display = "block";
//     }
// }

function yesnoCheck(that) {
    if (that.value == "ปกติ") {
        const element1 = document.getElementById("document2");
        const element2 = document.getElementById("document3");
        const element3 = document.getElementById("document4");

        element1.remove();
        element2.remove();
        element3.remove();
        
    } else {
        var a = document.createElement("div");
        a.setAttribute("class", "mt-2");
        a.setAttribute("id", "document2");

        var b = document.createElement("div");
        b.setAttribute("class", "mt-2");
        b.setAttribute("id", "document3");

        var c = document.createElement("div");
        c.setAttribute("class", "mt-2");
        c.setAttribute("id", "document4");

        var x = document.createElement("INPUT");
        x.setAttribute("type", "file");
        x.setAttribute("class", "form-control");
        x.setAttribute("name", "document2");
        x.setAttribute("accept", ".pdf");
        x.setAttribute("required", "");

        var y = document.createElement("INPUT");
        y.setAttribute("type", "file");
        y.setAttribute("class", "form-control");
        y.setAttribute("name", "document3");
        y.setAttribute("accept", ".pdf");
        y.setAttribute("required", "");

        var z = document.createElement("INPUT");
        z.setAttribute("type", "file");
        z.setAttribute("class", "form-control");
        z.setAttribute("name", "document4");
        z.setAttribute("accept", ".pdf");
        z.setAttribute("required", "");

        // Append to another element:
        document.getElementById("document-box").appendChild(a);
        document.getElementById("document2").append(x);

        document.getElementById("document-box").appendChild(b);
        document.getElementById("document3").append(y);

        document.getElementById("document-box").appendChild(c);
        document.getElementById("document4").append(z);
    }


    
}
