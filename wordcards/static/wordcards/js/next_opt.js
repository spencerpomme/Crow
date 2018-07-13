function next_opt() {
    // Common part of forget_opt() and remember_opt():
    // The 'Next' button of card view state 2 is pressed.

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
    tag.append("<div style=\"height:5px\" id='temp-div'></div>");
    tag.append("<button type=\"button\" class=\"btn btn-outline-danger\" id=\"forget\" onclick=\"forget_opt()\">Hmm...</button>");
    $("a.card-link").attr("style", "color: white");
    // (3) Thirdly, make new request, get new image, word_text, word_def and hint:
    let temp = Number($("div.store-word-id").text());
    $("div.store-word-id").text(temp+1);
    $.ajax({
        cache: false,
        type: "GET",
        url: "update",
        data: {'id': $("div.store-word-id").text()},
        async: true,
        dataType: 'json',
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
        },
        // Replace the corresponding content with newly received ones:
        success: function (res) {
            console.log(res);
            console.log(typeof res);
            console.log(res.word_text);
            $("h5#shift-word").text(res.word_text);
            $("p#shift-def").text(res.word_def);
            console.log(typeof res.id);
            console.log("res.id ->", res.id);
            $("div.store-word-id").text(res.id);
            $("img.card-img-top").attr("src", res.img_url);
        }
    })

    // (4) Lastly, change back text and definition:
    $("h5#shift-word").attr("style", "display: none");
    $("h5#shift-what").attr("style", "display: block");
    $("p#shift-hint").attr("style", "display: block");
    $("p#shift-def").attr("style", "display: none");
}
