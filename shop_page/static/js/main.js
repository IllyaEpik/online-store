import check from "./modules/capacity.js"
import add from "./modules/add.js"
import cordinate from "./modules/coordinate.js"
import modal from "./modules/modal.js"
import add_modal from "./modules/add_modal.js"
import image from "./modules/image.js"
check()
cordinate()
add()
modal()
add_modal()
image()

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
