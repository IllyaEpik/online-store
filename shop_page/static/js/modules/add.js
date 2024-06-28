function add(){
    let buttons = document.getElementsByClassName("buy")
    for (let count = 0; count < buttons.length; count++){
    let button = buttons[count]
    console.log(button,button.id)
    button.addEventListener("click", function (event) {
        if (document.cookie=="" || document.querySelector("#message").textContent=="0"){
            document.querySelector(".message").style.display = 'block'
            document.querySelector("#message").style.display = 'block'
            document.cookie=`products=${button.id};path=/`
            document.querySelector("#message").textContent = `1`
        }
        else{
            var cookie = document.cookie.split("=")[1]
            console.log('hello')
            cookie =  cookie + ' ' + button.id
            document.cookie = `products=${cookie};path=/`
            document.querySelector("#message").textContent = `${cookie.split(" ").length}`
            }
        })
    }
}
export default add