var i = 1;

function addinternWorks() {
    i++;

    var a = document.createElement("div");
	a.setAttribute("class", `col-6 internworks-left-${i} mt-2 pe-1`);
    a.setAttribute("id", `internworks-left-${i}`);

    // <input type="file" class="form-control" id="file-ip-1" name="image" accept="image/*" onchange="showPreview(event);" required></input>
    
    var b = document.createElement("div");
	b.setAttribute("class", `col-6 internworks-right-${i} mt-2 ps-1`);
    b.setAttribute("id", `internworks-right-${i}`);

    var c = document.createElement("div");
	c.setAttribute("class", `col-12 bottom-${i} mt-1`);
    c.setAttribute("id", `bottom-${i}`);

    var x = document.createElement("INPUT");
	x.setAttribute("type", "text");
	x.setAttribute("class", "form-control");
	x.setAttribute("name", "image");
	x.setAttribute("id", "lessonTitle");
    x.setAttribute("placeholder", `google, github, youtube, etc (${i})`);
	
    var y = document.createElement("INPUT");
	y.setAttribute("type", "text");
	y.setAttribute("class", "form-control");
	y.setAttribute("name", "imageTitle");
	y.setAttribute("id", "lessonTitle");
    y.setAttribute("placeholder", `ชื่อผลงาน (${i})`);

    var z = document.createElement("TEXTAREA");
	z.setAttribute("class", "form-control");
	z.setAttribute("name", "internworkDetail");
	z.setAttribute("id", "lessonTitle");
    z.setAttribute("cols", "30");
    z.setAttribute("rows", "2");
    z.setAttribute("placeholder", `รายละเอียดผลงาน (${i})`);

    document.getElementById("internworks-input-row").appendChild(a);
    document.getElementById("internworks-input-row").appendChild(b);
    document.getElementById("internworks-input-row").appendChild(c);
    
    // Append to another element:
    document.getElementById(`internworks-left-${i}`).append(x);
    document.getElementById(`internworks-right-${i}`).append(y);
    document.getElementById(`bottom-${i}`).append(z);


    // document.getElementById('lesson-input-row').append(x);
	// document.getElementById('lesson-input-row').append(y);
}