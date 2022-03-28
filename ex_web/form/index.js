function main(){
    let a = Number(document.getElementById('input-a').value);
    let b = Number(document.getElementById('input-b').value);
    let total = (a + b);
    document.getElementById("reuslt").style.display = "block";
    document.getElementById('reuslt').innerText = "Total : " + total;
}

