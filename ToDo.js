var myform = document.getElementById("myform")
var myform = document.getElementById("myitem")
var myform = document.getElementById("myinput")
myform.addEventListener('submit',
    function(event){
        createitem(myinput.value)
    }
)
function createitem(inputitems){
    var item = `<li> ${inputItems}
    <Button onclick="deleteElement(this)">delete/button></li
    `
    myitem.value=""
    myinput.focus()
}

function deleteElement(ElementToDelete){
    ElementToDelete.parentElement.remove()
}
