function next_opt() {
    // Common part of forget_opt() and remember_opt():
    // The button of card view state 1 is pressed.
    // (1) Firstly, update the progressbar:
    let percent = document.getElementById("progressBar").innerHTML;
    percent = Number(percent.replace("%", ""));
    if (percent < 100) {
        percent += 20;
        document.getElementById("progressBar").innerText = percent + "%";
        document.getElementById("progressBar").style.width = percent + "%";
    } else {
        // do nothing.
    }
    // (2) Secondly, change UI components from state-2 back to state-1:
    $("button").remove("#next");
    $("div").remove("#temp-div");
    let tag = $("ul#button-place-marker");
    tag.append("<button type=\"button\" class=\"btn btn-outline-success\" id=\"remember\" onclick=\"remember_opt()\">I know it</button>")
    tag.append("<div style=\"height:5px\"></div>");
    tag.append("<button type=\"button\" class=\"btn btn-outline-danger\" id=\"forget\" onclick=\"forget_opt()\">Hmm...</button>");
    $("a.card-link").attr("style", "color: white");
    // (3) Thirdly, make new request, get new image, word_text, word_def and hint:

    // (4) Fourthly, replace the corresponding content with newly received ones:

    // (5) Lastly, change back text and definition:
    $("h5#shift-word").attr("style", "display: none");
    $("h5#shift-what").attr("style", "display: block");
    $("p#shift-hint").attr("style", "display: block");
    $("p#shift-def").attr("style", "display: none");
}
