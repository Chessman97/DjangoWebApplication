$(document).ready(function(){
    $(".del_button").click(function()
    {
        var id = $(this).data("id");
        $.ajax(
            {
            url: 'delete/'+id,
            success: function(data)
            {
                $("#del"+id).remove();
            },
            error: function(data)
            {
                alert("error");
            }
        });
    });

    $("#save_button").click(function(){
        var name = $("#name_input").val();
        var modell = $("#modell_input").val();
        var marka = $("#marka_input").val();
        var gruz = $("#gruz_input").val();
        var massa = $("#massa_input").val();
        var dvig = $("#dvig_input").val();
        var cost = $("#cost_input").val();
        var csrfmiddlewaretoken = $("input[type=hidden]").val();

        $.ajax({
            type: "POST",
            url: "create/",
            data: {
                name: name,
                modell: modell,
                marka: marka,
                gruz: gruz,
                massa: massa,
                dvig: dvig,
                cost: cost,
                csrfmiddlewaretoken : csrfmiddlewaretoken
            },
            success: function(data) {
                //alert("Товар добавлен!");
            },
            error: function(data) {
                alert("error");
            }
        });
    });

    $("#update_button").click(function(){
        var id = $("#id").val();
        var name = $("#name_input").val();
        var modell = $("#modell_input").val();
        var marka = $("#marka_input").val();
        var gruz = $("#gruz_input").val();
        var massa = $("#massa_input").val();
        var dvig = $("#dvig_input").val();
        var cost = $("#cost_input").val();
        var csrfmiddlewaretoken = $("input[type=hidden]").val();
        alert(name+modell+marka+gruz+massa+dvig+cost+id);
        $.ajax({
            type: "POST",
            url: "/",
            data: {
                name: name,
                modell: modell,
                marka: marka,
                gruz: gruz,
                massa: massa,
                dvig: dvig,
                cost: cost,
                csrfmiddlewaretoken : csrfmiddlewaretoken
            },
            success: function(data) {
                alert("Товар изменен!");
            },
            error: function(data) {
                alert("error");
            }
        });
    });
}) ;