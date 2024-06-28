function cordinate(){
    document.querySelector("#message").style.top = `-19`
    let deleteP = document.getElementsByClassName("deleteP")
    let deleteImg = document.getElementsByClassName("deleteImg")
    let y = 420
    for (let count = 0; count < deleteImg.length; count++){
        deleteImg[count].style.top = y
        deleteP[count].style.top = y
        y += 320
    }
    if (document.cookie=="" || document.querySelector("#message").textContent=="0"){
        console.log(document.querySelector("#message").innerHTML)
        document.querySelector(".message").style.display = 'none'
        document.querySelector("#message").style.display = 'none'
    }
}
export default cordinate