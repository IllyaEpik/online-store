let buttons = document.getElementsByClassName("buy")
let edits = document.getElementsByClassName("editorButton")
console.log(buttons)

if (document.cookie=="" || document.querySelector("#message").textContent=="0"){
    console.log(document.querySelector("#message").innerHTML)
    document.querySelector(".message").style.display = 'none'
    document.querySelector("#message").style.display = 'none'
}
function cordinate(){
    let names = document.getElementsByClassName("name")
    let discountButton = document.getElementsByClassName("discountButton")
    let priceButton = document.getElementsByClassName("priceButton")
    // let ctx= document.getElementById("canvas").getContent("2d")
    let h = document.querySelectorAll("h1")
    let discount = document.getElementsByClassName("discount")
    let price = document.getElementsByClassName("price")
    for (let count = 0; count < discount.length; count++){
        // names[count].style.left = 1000
        // names[count].style.top = count*321+145
        priceButton[count].style.top = count*321+180
        priceButton[count].style.left = 450 
        discountButton[count].style.left = 475
        discountButton[count].style.top = count*321+210
        // console.log(h[count].textContent.length*10)
    }

}
function check(){
    let white = document.querySelectorAll(".white")
    
    // document.querySelector('.white')
    let orange = document.querySelectorAll(".orange")
    console.log(white , orange)
    for (let count = 0; count < white.length; count++){
        white[count].style.background = "white"
    }
    for (let count = 0; count < orange.length; count++){
        orange[count].style.background = "#EFCB4A"
    }
}
check()
let capacityButtons = document.querySelectorAll(".capacityButton")

for (let count = 0; count < capacityButtons.length; count++){
    capacityButtons[count].addEventListener("click", function (event){
        
        for (let count1 = 0; count1 < capacityButtons.length; count1++){
            if (capacityButtons[count].id==capacityButtons[count1].id){
                capacityButtons[count1].style.background = "white"
            }
        }
        capacityButtons[count].style.background = "#EFCB4A"
    })
}
cordinate()
// cordinate()
// document.querySelector('h1').style.marginTop
// buttons[0].onclick = () =>{
//    console.log(11)
// }
// lick()
// let ar (event) => {
// let array = [0,1,2,3,4,5,6,7]
// let butt?on = 0|
// if (edits.length || false){
//     // cordinate()
//     console.log(edits)
//     let names = document.getElementsByClassName("name")
//     let discountButton = document.getElementsByClassName("discountButton")
//     let priceButton = document.getElementsByClassName("priceButton")

//     let h = document.querySelectorAll("h1")
//     let discount = document.getElementsByClassName("discount")
//     let price = document.getElementsByClassName("price")
    
//     for (let count = 0; count < names.length; count++){
//         names[count].addEventListener("click", function (event){
//             h[count].textContent=prompt("Вкажіть назві продукту", h[count].textContent)
//             // names[count].style.left = 325+h[count].textContent.length*10
//         }) 
//     }
//     for (let count = 0; count < discount.length; count++){
//         discountButton[count].addEventListener("click", function (event){
//             discount[count].textContent = "Знижка "+ Number(prompt("Вкажіть знижку продукту", discount[count].textContent))+"%"
//         }) 
//     }
//     for (let count = 0; count < price.length; count++){
//         priceButton[count].addEventListener("click", function (event){
//             price[count].textContent = Number(prompt("Вкажіть ціну продукту", price[count].textContent))+" грн"
//         }) 
//     }
// }
document.querySelector("#message").style.top = `-19`
for (let count = 0; count < buttons.length; count++){
        // button=document.getElementById()
        // button.style.margineleft
    // console.log(count)
    // let button = buttons[0]
    // console.log(button.COMMENT_NODE)
    let button = buttons[count]
    console.log(button,button.id)

    button.addEventListener("click", function (event) {
        // 
        if (document.cookie=="" || document.querySelector("#message").textContent=="0"){
            document.querySelector(".message").style.display = 'block'
            document.querySelector("#message").style.display = 'block'
            document.cookie=`products=${button.id};path=/`
            document.querySelector("#message").textContent = `1`
            // document.querySelector("#message").style.height = `1`
        }
        else{
            var cookie = document.cookie.split("=")[1]
            console.log('hello')
            // console.log("end", cookie) 
            cookie =  cookie + ' ' + button.id
            document.cookie = `products=${cookie};path=/`
            document.querySelector("#message").textContent = `${cookie.split(" ").length}`


        }
    // butto
    })
}
// })