function center(element){
    element.style.marginLeft = 'auto'
    element.style.marginRight = 'auto'
    element.style.left = 'auto'
    element.style.right = 'auto'
}
function oformed(){
    let button=document.querySelector(".form")
    let price=document.querySelector(".all-price")
    let price_name = document.querySelector(".price-name")
    let img = document.querySelectorAll(".img-product")
    let start = document.querySelectorAll(".start")
    let border = document.querySelectorAll(".border")
    let counts = document.querySelectorAll("#count")
    let name = document.querySelectorAll(".product-name")
    let edit = document.querySelectorAll('.edit')
    let h3 = document.querySelectorAll('.price-h3')
    let div = document.querySelectorAll('.price-div')
    let h2 = document.querySelectorAll('.price-h2')
    try{
        price_name.style.display = 'flex'
        price.style.position = 'unset'
        price.style.display = 'flex'
        price.style.flexDirection = 'row'
        price_name.style.flexDirection = 'row'
        price_name.style.justifyContent = 'center'
    }catch{
        
    }
    for (let count = 0; count < start.length; count++){

        start[count].style.display = 'flex'
        start[count].style.justifyContent = 'center'
        border[count].style.alignItems = 'center'
        border[count].style.display = 'flex'
        border[count].style.position = 'unset'
        edit[count].style.position = 'unset'
        h3[count].style.position = 'unset'
        div[count].style.position = 'unset'
        counts[count].style.position = 'unset'

        edit[count].style.display = 'flex'
        h3[count].style.display = 'flex'
        div[count].style.display = 'flex'
        counts[count].style.display = 'flex'
        name[count].style.display = 'flex'
        name[count].style.justifyContent = 'center'
        border[count].style.justifyContent = 'center'
        start[count].style.marginTop = 20
        counts[count].style.width=100
        div[count].style.width=200
        div[count].style.justifyContent = 'center'
        div[count].style.alignItems = 'center'
        h3[count].style.textAlign = 'center'
        h2[count].style.textAlign = 'center'
        counts[count].style.justifyContent = 'center'
        counts[count].style.textAlign = 'center'
        counts[count].style.height=0
    }
    
    center(button)
}
export default oformed