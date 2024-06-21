
function image(){
    let inputs = document.querySelectorAll("input")
    let filenames = document.querySelectorAll(".filename")
    for(let count = 0; count < inputs.length; count++){
        inputs[count].addEventListener("change", function (){
            if(inputs[count].type == "file"){
                console.log(inputs[count].files[0].name)
                for(let count1 = 0; count1 < filenames.length; count1++){

                    filenames[count1].textContent = inputs[count].files[0].name
                }
            }

                
        })
    }
}
export default image