function modal(){
    let names = document.getElementsByClassName("name")
    let priceList = document.querySelectorAll(".priceButton")
    let discountList = document.querySelectorAll(".discountButton")
    let imgList = document.getElementsByClassName("img")
    let modal = document.querySelector(".modal-window")
    let background = document.querySelector(".background")
    let nameEdit = document.querySelector(".name-edit")
    let modalInput = document.querySelector(".modal-input")
    let sendButton = document.querySelector(".send-button")
    let labelImg = document.querySelector(".label-img")
    // console.log(priceList)//
    function text(dataList,value){
        for (let count = 0; count < dataList.length; count++){
            let data = dataList[count]
            data.addEventListener("click", ()=>{
                background.style.display = "block"
                modal.style.display = "flex"
                nameEdit.textContent = "change text"
                modalInput.type = "text"
                modalInput.style.borderRadius = "10px"
                modalInput.style.height = "74px"
                modalInput.style.width = "450px"
                sendButton.value = data.value + value
                labelImg.style.display = "none"
            })
        }
        
    }
    text(priceList, ";PRICE")
    text(names, ";NAME")
    text(discountList, ";DISCOUNT")
    for (let count = 0; count < imgList.length; count++){
        let img = imgList[count]
        img.addEventListener("click", ()=>{
            background.style.display = "block"
            modal.style.display = "flex"
            modalInput.id = "img"
            modalInput.style.display= "none"
            // nameEdit.textContent = "change text"
            // modalInput.type = "text"
            // modalInput.style.borderRadius = "10px"
            // modalInput.style.height = "74px"
            // modalInput.style.width = "450px"
            // 
            modalInput.accept = 'image/*'
            sendButton.value = img.value + ";IMG"
        })
    }
}
export default modal