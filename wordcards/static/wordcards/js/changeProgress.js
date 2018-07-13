function changeProgress() {
    let percent = document.getElementById("progressBar").innerHTML;
    percent = Number(percent.replace("%", ""));
    if (percent < 100) {
        percent += 10;
        document.getElementById("progressBar").innerText = percent + "%";
        document.getElementById("progressBar").style.width = percent + "%";
    } else {
        // do nothing.
    }
}
