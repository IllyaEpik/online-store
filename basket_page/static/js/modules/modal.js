function modal(){
    console.log
    let form=document.querySelector(".modal")
    document.querySelector(".form").addEventListener("click", () => (
        form.style.display = "flex"
    ))
}

export default modal