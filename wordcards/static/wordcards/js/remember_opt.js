function remember_opt() {
    // Common part of forget_opt() and remember_opt():
    // The 'I know it' button of card view state 1 is pressed.

    // (1) Change UI components from state-1 to state-2:
    $("button").remove("#remember, #forget");
    $("div").remove("#temp-div");
    let tag = $("ul#button-place-marker");
    tag.append("<div style=\"height:5px\" id='temp-div'></div>");
    tag.append("<button type=\"button\" class=\"btn btn-outline-primary\" id=\"next\" onclick=\"next_opt()\">Next</button>");
    $("a.card-link").attr("style", "color: gray");

    // (2) Change text and definition:
    $("h5#shift-word").attr("style", "display: block");
    $("h5#shift-what").attr("style", "display: none");
    $("p#shift-hint").attr("style", "display: none");
    $("p#shift-def").attr("style", "display: block");
}

