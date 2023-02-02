function update_tpa(player_number){
    var balls_el = document.getElementById("balls_" + player_number.toString());
    var errors_el = document.getElementById("errors_" + player_number.toString());

    var balls = parseInt(balls_el.value);
    var errors = parseInt(errors_el.value);

    var tpa = 0;
    if (balls != 0 || errors != 0){
        tpa = balls / (balls + errors);
        tpa = Math.round(1000 * tpa) / 1000;
    }

    var tpa_el = document.getElementById("tpa_" + player_number.toString());
    tpa_el.value = tpa;

    write_to_files();
}

function write_to_files(){
    var all_dymanic_els = document.getElementsByClassName("dynamic_el");
    var request_body = {};

    for (var i = 0; i < all_dymanic_els.length; i++){
        var el = all_dymanic_els[i];
        var id = el.id;
        request_body[id] = el.value;
    }

    var url = "/write_to_files";
    var xhttp = new XMLHttpRequest();
    xhttp.onload = function(){
        show_success_alert();
    }
    xhttp.open("POST", url, true);
    xhttp.setRequestHeader('Content-type', 'application/json; charset=UTF-8');
    xhttp.send(JSON.stringify(request_body));
}


function show_success_alert(){
    var btn = document.getElementById("submit_btn");
    btn.innerHTML = "Fertig!";
    setTimeout(function(){
        var btn = document.getElementById("submit_btn");
        btn.innerHTML = "Werte schreiben";
    }, 2000);
}
