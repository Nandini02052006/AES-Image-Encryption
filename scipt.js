function encryptImage(){

let file = document.getElementById("imageInput").files[0]
let key = document.getElementById("key").value

let formData = new FormData()
formData.append("image",file)
formData.append("key",key)

fetch("/encrypt",{
method:"POST",
body:formData
})
.then(res=>res.json())
.then(data=>{
document.getElementById("result").innerText=data.message
})

}

function decryptImage(){

let file = document.getElementById("imageInput").files[0]
let key = document.getElementById("key").value

let formData = new FormData()
formData.append("image",file)
formData.append("key",key)

fetch("/decrypt",{
method:"POST",
body:formData
})
.then(res=>res.json())
.then(data=>{
document.getElementById("result").innerText=data.message
})

}