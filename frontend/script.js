var url = "http://127.0.0.1:5000/students";

function listar(list) {
    let text = "<table border='1'> <tr> <th>CPF</th><th>Nome</th><th>Idade</th><th>Email</th><th>Média</th><th>Histórico</th><th>Turma</th>";
    for (let x in list) {
      text += "<tr>";
      text += "<td>" + list[x].CPF + "</td>";
      text += "<td>" + list[x].nome + "</td>";
      text += "<td>" + list[x].idade + "</td>";
      text += "<td>" + list[x].email + "</td>";
      text += "<td>" + list[x].media + "</td>";
      text += "<td>" + list[x].historico + "</td>";
      text += "<td>" + list[x].id_turma + "</td>";
      text += "</tr>";
    }
    text += "</table>";

    return text;

}

function request(status, element) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.status == status) {
            const myObj = JSON.parse(this.responseText);   
            console.log(myObj.students)
            document.getElementById(element).innerHTML = listar(myObj.students);
      }
    };

    return xhttp;
}


function listarTodos() {
    var xhttp = request(200, "listar_todos_table")

    xhttp.open("GET", url, true);
    xhttp.send();
}

function listarUm() {
    var x = document.getElementById("listar_um");

    var xhttp = request(200, "listar_um_table")

    var thisUrl = url + "/" + x.elements[0].value;
    xhttp.open("GET", thisUrl, true);
    xhttp.send();
}

function add() {
    var x = document.getElementById("add");

    var xhttp = request(201, "add_table");

    let json = '{ "CPF" : ' +  '"' + x.elements[0].value + '" ,' +
                ' "nome" : ' + '"' + x.elements[1].value + '" ,' +
                ' "idade" : ' + '"' + x.elements[2].value + '" ,' +
                ' "email" : ' + '"' + x.elements[3].value + '" ,' +
                ' "media" : ' + '"' + x.elements[4].value + '" ,' +
                ' "historico" : ' + '"' + x.elements[5].value + '" ,' +
                ' "id_turma" : ' + '"' + x.elements[6].value + '" }';
    
    xhttp.open("POST", url, true);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(json);
    
}

function update() {
    var x = document.getElementById("update");

    let json = '{ "CPF" : "' + x.elements[0].value + '" ,';

    if (x.elements[1].value !== "")
        json += ' "nome" : ' + '"' + x.elements[1].value + '" ,';
    if (x.elements[2].value !== "")
        json += ' "idade" : ' + '"' + x.elements[2].value + '" ,';
    if (x.elements[3].value !== "")
        json += ' "email" : ' + '"' + x.elements[3].value + '" ,';
    if (x.elements[4].value !== "")
        json += ' "media" : ' + '"' + x.elements[4].value + '" ,';
    if (x.elements[5].value !== "")
        json += ' "historico" : ' + '"' + x.elements[5].value + '" ,';
    if (x.elements[6].value !== "")
        json += ' "id_turma" : ' + '"' + x.elements[6].value + '" ,';

    json = json.slice(0, -1)
    json += "}"
    
    var xhttp = request(200, "update_table");

    var thisUrl = url + "/" + x.elements[0].value;
    xhttp.open("PUT", thisUrl, true);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(json);
}

function deletar() {
    var x = document.getElementById("deletar");

    var xhttp = request(200, "deletar_table")

    var thisUrl = url + "/" + x.elements[0].value;
    xhttp.open("DELETE", thisUrl, true);
    xhttp.send();
}