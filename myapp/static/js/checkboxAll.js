
function toggle1(oInput) {
    var aInputs = document.getElementsByName('check1[]');
    for (var i=0;i<aInputs.length;i++) {
        if (aInputs[i] != oInput) {
            aInputs[i].checked = oInput.checked;
        }
    }
}

function toggle2(oInput) {
    var aInputs = document.getElementsByName('check2[]');
    for (var i=0;i<aInputs.length;i++) {
        if (aInputs[i] != oInput) {
            aInputs[i].checked = oInput.checked;
        }
    }
}


