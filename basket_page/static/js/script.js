let plusButtons = document.querySelectorAll(".edit2")
let minusButtons = document.getElementsByClassName("edit1")
let countText = document.querySelectorAll("#count")
// if (plusButtons.length = )
function cordinate(){
    let y = 175
    let borders = document.querySelectorAll(".border")
    let listCount = document.querySelectorAll("#count")
    let listEdit = document.querySelectorAll(".edit")
    let listPriceDiv = document.querySelectorAll(".price-div")
    let listH3 = document.querySelectorAll(".price-h3")
    // countTag.previousElementSibling
    let countTag = document.querySelector(".count-products")
    let allPrice = document.querySelector(".all-price")
    let disCountTag = document.querySelector(".discount")
    // listEdit[0].style.top = 75
    // listCount[0].style.top = -20
    // borders[0].style.top = 175
    let disCount=0
    let countProducts=0
    let priceProducts=0
    for (let count = 0; count < borders.length; count++){
        countProducts+=Number(listCount[count].textContent)
        let price = Number(listH3[count].previousElementSibling.id)*Number(listCount[count].textContent)
        priceProducts+=price
        listH3[count].previousElementSibling.textContent= price
        let disCounting = Number(listH3[count].id)
        disCounting = disCounting/100*Number(listH3[count].previousElementSibling.id)
        disCounting = disCounting*Number(listCount[count].textContent)
        disCount +=  disCounting
        // countTag.nextElementSibling.style.left=60
        borders[count].style.top = y+count*300
        listCount[count].style.top = -20
        listEdit[count].style.top = 75
        listPriceDiv[count].style.top = 60
        // listH3[count].previousElementSibling
        // console.log(listH3[count].previousElementSibling.style.width)
        listH3[count].style.left = 60
        listH3[count].style.top = 8
    }
    
    let text = countTag.textContent.split("-")
    text[0]=countProducts
    countTag.textContent=text.join("-")
    countTag.nextElementSibling.textContent=`${priceProducts} грн`

    allPrice.textContent=`${priceProducts-disCount} грн`
    disCountTag.textContent=`${disCount} грн`
}
// console.log(plusButtons,document.getElementsByClassName("edit2").length)
// console.log(minusButtons)
function destroy(){
    let divs = document.querySelectorAll(".start")
    // console.log(divs)
    for (let count = 0; count < divs.length; count++){
        // console.log(id)
        let div = divs[count]
        let id = div.id
        try{
        let cookie = document.cookie.split("=")[1].split(" ")
        
        let count1 = 0
        // console.log(cookie)
        for (let count2 = 0; count2 < cookie.length; count2++ ){
            // console.log(`${cookie[count]}`)/
            if (`${cookie[count2]}`==`${id}`){
                count1++
            }
        }
        
        if(count1 == 0){
            div.remove()
        }
        }catch{
            div.remove()
            
        }
    }
    if (document.querySelectorAll(".start").length==0){
        document.querySelector("#empty").style.display="block"
        document.querySelector("#message").style.display="none"
        document.querySelector(".message").style.display="none"
        document.cookie = ""

    }
    cordinate()
}
destroy()


function counting (id){
    // console.log(id)
    let text = countText[id-1]
    let cookie = document.cookie.split("=")[1].split(" ")
    document.querySelector("#message").textContent = `${cookie.length}`
    let count1 = 0
    // console.log(cookie)
    for (let count = 0; count < cookie.length; count++ ){
        // console.log(`${cookie[count]}`)
        if (`${cookie[count]}`==`${id}`){
            count1++
        }
    }
    
    text.textContent = `${count1}`
    destroy()
}

for (let count = 0; count < plusButtons.length; count++){
    let button = plusButtons[count]
    let id = button.id
    counting(id)
    button.addEventListener("click", function (event){
        if (document.cookie==""){
            // document.querySelector(".message").style.display = 'block'
            // document.querySelector("#message").style.display = 'block'
            document.cookie=`products=${id};path=/`
        }
        else{
            var cookie = document.cookie.split("=")[1]
            console.log('hello')
            // console.log("end", cookie) 
            cookie =  cookie + ' ' + id
            document.cookie = `products=${cookie};path=/`
            counting(id)
            // document.querySelector("#message").textContent = `${cookie.split(" ").length-1}`

        }
    })
    // console.log(2)
}
for (let count = 0; count < minusButtons.length; count++){
    let button = minusButtons[count]
    button.addEventListener("click", function (event){
        if (document.cookie==""){
            // document.querySelector(".message").style.display = 'block'
            // document.querySelector("#message").style.display = 'block'
            // document.cookie=`products=${button.id};path=/`
        }
        else{
            var cookie = document.cookie.split("=")[1].split(" ")
            // console.log('hello')
            // console.log("end", cookie) 
            cookie.splice(cookie.indexOf(button.id),1)
            document.cookie = `products=${cookie.join(" ")};path=/`
            // document.querySelector("#message").textContent = `${cookie.split(" ").length-1}`
            // console.log((12))
            counting(button.id)
        }

})}