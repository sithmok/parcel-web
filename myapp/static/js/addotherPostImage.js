var n = 1;

function addotherPostImage() {
    n++;

    var a = document.createElement("div");
	a.setAttribute("class", `col-6 left-${n} mt-1 pe-1`);
    a.setAttribute("id", `left-${n}`);

    // <input type="file" class="form-control" id="file-ip-1" name="image" accept="image/*" onchange="showPreview(event);" required></input>
    
    var b = document.createElement("div");
	b.setAttribute("class", `col-6 right-${n} mt-1 ps-1`);
    b.setAttribute("id", `right-${n}`);

    var x = document.createElement("INPUT");
	x.setAttribute("type", "file");
	x.setAttribute("class", "form-control");
	x.setAttribute("name", "image");
	x.setAttribute("id", "lessonTitle");
	
    var y = document.createElement("INPUT");
	y.setAttribute("type", "text");
	y.setAttribute("class", "form-control");
	y.setAttribute("name", "imageTitle");
	y.setAttribute("id", "lessonTitle");
    y.setAttribute("placeholder", `ชื่อรูปภาพ (${n})`);
    
    document.getElementById("lesson-input-row").appendChild(a);
    document.getElementById("lesson-input-row").appendChild(b);
    
   
    // Append to another element:
    document.getElementById(`left-${n}`).append(x);
    document.getElementById(`right-${n}`).append(y);


    // document.getElementById('lesson-input-row').append(x);
	// document.getElementById('lesson-input-row').append(y);
}