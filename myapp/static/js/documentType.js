// function selectElement() {
// 	let document1 = document.getElementsByClassName('document1')
// 	let document2 = document.getElementsByClassName('document2')
//     let document3 = document.getElementsByClassName('document3')
//     let document4 = document.getElementsByClassName('document4')

// 	const selectType  = document.querySelector('.documentType').value;

// 		if (selectType === "ปกติ"){
// 			document1.style.display = "block";
// 			document2.style.display = "none";
// 			document3.style.display = "none";
// 			document4.style.display = "none";
// 			}
// 		else {
// 			document1.style.display = "none";
// 			document2.style.display = "block";
// 			document3.style.display = "block";
// 			document4.style.display = "block";
// 		}
// }

function yesnoCheck(that) {
    if (that.value == "ปกติ") {
        document.getElementById("document1").style.display = "block";
        document.getElementById("document2").style.display = "none";
        document.getElementById("document3").style.display = "none";
        document.getElementById("document4").style.display = "none";
    } else {
        document.getElementById("document1").style.display = "block";
        document.getElementById("document2").style.display = "block";
        document.getElementById("document3").style.display = "block";
        document.getElementById("document4").style.display = "block";
    }
}
