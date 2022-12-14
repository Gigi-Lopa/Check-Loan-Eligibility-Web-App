$("document").ready(function (){
    $("#tabs").tabs()
})

function handleUserNames(){
    document.querySelectorAll("th[id='userId']").forEach(row=>{

    })
}
document.addEventListener("DOMContentLoaded", ()=>{
    document.querySelectorAll("td[id='loanAmount']").forEach(row =>{
        let loanamont = parseInt(row.textContent)
        $(row).empty()
        $(row).append((loanamont*1000))
    })
})

