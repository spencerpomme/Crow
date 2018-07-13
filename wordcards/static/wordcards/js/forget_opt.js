function forget_opt() {
    // Common part of forget_opt() and remember_opt():
    // The 'Hmm...' button of card view state 1 is pressed.

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

    // (2) Secondly, change UI components from state-1 to state-2:
    $("button").remove("#remember, #forget");
    $("div").remove("#temp-div");
    let tag = $("ul#button-place-marker");
    tag.append("<div style=\"height:5px\" id='temp-div'></div>");
    tag.append("<button type=\"button\" class=\"btn btn-outline-primary\" id=\"next\" onclick=\"next_opt()\">Next</button>");
    $("a.card-link").attr("style", "color: gray");

    // (3) Thirdly, change text and definition:
    $("h5#shift-word").attr("style", "display: block");
    $("h5#shift-what").attr("style", "display: none");
    $("p#shift-hint").attr("style", "display: none");
    $("p#shift-def").attr("style", "display: block");
}
