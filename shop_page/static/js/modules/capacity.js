function check(){
    let white = document.querySelectorAll(".white")
    let orange = document.querySelectorAll(".orange")
    console.log(white , orange)
    for (let count = 0; count < white.length; count++){
        white[count].style.background = "white"
    }
    for (let count = 0; count < orange.length; count++){
        orange[count].style.background = "#EFCB4A"
    }
    let capacityButtons = document.querySelectorAll(".capacityButton")

    for (let count = 0; count < capacityButtons.length; count++){
        capacityButtons[count].addEventListener("click", function (event){
            
            for (let count1 = 0; count1 < capacityButtons.length; count1++){
                if (capacityButtons[count].id==capacityButtons[count1].id){
                    capacityButtons[count1].style.background = "white"
                }
            }
            capacityButtons[count].style.background = "#EFCB4A"
        })}
}
export default check 