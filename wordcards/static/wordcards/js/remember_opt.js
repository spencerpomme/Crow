function remember_opt() {
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
    // (2) Secondly, change UI components from state-1 to state-2:
    $("button").remove("#remember, #forget");
    let tag = $("ul#button-place-marker");
    tag.append("<div style=\"height:5px\"></div>");
    tag.append("<button type=\"button\" class=\"btn btn-outline-primary\" id=\"forget\" onclick=\"#\">Next</button>");
}
    /*
    $.ajax({
        cache: false,
        type: "POST",
        url: "{% url 'index' %}",
        data: {'id': id, 'type': type, 'amount': amount},
        async: true,
        //<!--需要将csrf_token传到request的header里，否则无法通过验证-->
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
        },
        success: function (data) {
            var content = document.getElementById("content")
            var div_container = document.getElementById("container")
            var new_div = document.createElement("div")
            if (data.status == 'fail') {
                new_div.id = "noid"
                new_div.className = "alert alert-danger alert-dismissible"
                new_div.role = "alert"
                if (data.type == "NoID") {
                    $('#balance').html(0)
                    $('#id').html("Null")
                    new_div.innerHTML = "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>\n" +
                        "          <strong>No Such UID !</strong>"
                    div_container.insertBefore(new_div, content)
                }

                if (data.type == "ValueError") {
                    new_div.innerHTML = "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>\n" +
                        "          <strong>Amount Must Be Integer !</strong>"
                    div_container.insertBefore(new_div, content)
                }

                if (data.type == "NoEnoughMoney") {
                    new_div.innerHTML = "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>\n" +
                        "          <strong>No Enough Balance !</strong>"
                    div_container.insertBefore(new_div, content)
                }

            } else if (data.status == 'success') {
                new_div.id = "success"
                new_div.className = "alert alert-success alert-dismissible"
                new_div.role = "alert"
                if (data.type == 'save') {
                    $('#balance').html(data.balance)
                    new_div.innerHTML = "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>\n" +
                        "<strong>Successfully Save  " + $('#save_amount').val() + " !</strong>"
                    div_container.insertBefore(new_div, content)
                }
                if (data.type == 'withdraw') {
                    $('#balance').html(data.balance)
                    new_div.innerHTML = "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\"><span aria-hidden=\"true\">&times;</span></button>\n" +
                        "<strong>Successfully Witdraw  " + $('#withdraw_amount').val() + " !</strong>"
                    div_container.insertBefore(new_div, content)
                }
                if (data.type == 'search') {
                    $('#balance').html(data.balance)
                    $('#id').html(data.id)
                }
            }
        },
    });
}


$('.search').on('click', function () {
    if ($('#user_id').val() == "")
        alert("Please Input UID !")
    else
        remember_opt($(this), 'search', $('#user_id').val(), 0);
});

$('.save').on('click', function () {
    if ($('#save_amount').val() == "")
        alert("Amount Can Not Be Empty !")
    else
        remember_opt($(this), 'save', $('#user_id').val(), $('#save_amount').val());
});

$('.withdraw').on('click', function () {
    if ($('#withdraw_amount').val() == "")
        alert("Amount Can Not Be Empty !")
    else
        remember_opt($(this), 'withdraw', $('#user_id').val(), $('#withdraw_amount').val());
});
*/
