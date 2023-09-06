
// display image preview
const elements = Array.from(document.querySelectorAll("#id_recto, #id_verso"))
const rotation_button = Array.from(document.querySelectorAll("form img[alt='rotate']"));
let rot = [0,0];

elements.forEach(element => {
                 addEventListener("change", (e) => showPreview(e.target))
                }
                );

function showPreview(element){
    if(element.files.length > 0){
        var src = URL.createObjectURL(element.files[0]);
        var preview = document.querySelector(`.${element.id} img`);
        preview.src = src;
        let i = elements.indexOf(element);
        rotation_button[i].style.display = 'inline-block';
        rot[i] = 0;
        document.querySelector("#id_rot").value = `${rot[0]},${rot[1]}`;
        preview.style.transform = `rotateZ(0deg)`;
    }
    }

run_button = document.querySelector("input[type='submit']")
run_button.addEventListener("click", (e) => {
    if (elements[0].value != ''  & elements[1].value != ''){
    frame = document.querySelector(".load");
    frame.style.display = "flex";}
})


// reset input field when loading page    
window.addEventListener("unload", clearInputField);

function clearInputField() {
    elements.forEach(element => {
        if(element.files.length > 0){   
         element.value='';
         rot = "0,0"}
    });
}



// rotate image
rotation_button.forEach(element => {
    element.addEventListener("click", (e) => rotate(e.target))
   }
   );


function rotate(element){
    let j = rotation_button.indexOf(element) 
    target = elements[j]
    preview = document.querySelector(`.${target.id} img[alt='id-card']`);
    rot[j] += 90;
    preview.style.transform = `rotateZ(${rot[j]}deg)`
    document.querySelector("#id_rot").value = `${rot[0]},${rot[1]}`
}

// change image size with rotation

