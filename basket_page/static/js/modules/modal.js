function modal(){
    console.log
    let form=document.querySelector(".modal")

    document.querySelector(".form").addEventListener("click", () => {
        form.style.display = "flex"
        document.querySelector(".submit").value=document.querySelector(".all-price").textContent
    })
}

export default modal