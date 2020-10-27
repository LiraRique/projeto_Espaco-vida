function editar(e){

    var linha = $(e).closest("tr");  // Para acrescentar um novo campo para aparecer no modal, só ir adicionado conforme está abaixo
    
    var nomeUsuario = linha.find("td:eq(1)").text().trim(); // texto da primeira coluna
    var cpfUsuario = linha.find("td:eq(2)").text().trim(); 
   
    var cep = linha.find("td:eq(5)").text().trim(); 
    var cidade = linha.find("td:eq(6)").text().trim(); 
    var uf = linha.find("td:eq(7)").text().trim(); 
    var endereco = linha.find("td:eq(8)").text().trim(); 
    var numeroendereco = linha.find("td:eq(9)").text().trim(); 
    var telefone = linha.find("td:eq(10)").text().trim(); 
    var celular = linha.find("td:eq(11)").text().trim(); 
    var artrose = linha.find("td:eq(12)").text().trim(); 
    var protusao_ernia_disco = linha.find("td:eq(13)").text().trim(); 
    var cirurgia = linha.find("td:eq(14)").text().trim(); 
    var medicacao = linha.find("td:eq(15)").text().trim(); 
    var email = linha.find("td:eq(16)").text().trim(); 
    var queixas_atuais = linha.find("td:eq(17)").text().trim(); 
   
    $("#nome_usuario").val(nomeUsuario);
    $("#cpf").val(cpfUsuario);
   
   
    $("#cep").val(cep);
    $("#cidade").val(cidade);
    $("#uf").val(uf);
    $("#endereco").val(endereco);
    $("#numero_endereco").val(numeroendereco);
    $("#telefone").val(telefone);
    $("#celular").val(celular);
    $("#artrose").val(artrose);
    $("#protusao").val(protusao_ernia_disco);
    $("#cirurgia").val(cirurgia);
    $("#medicacao").val(medicacao);
    $("#email").val(email);
    $("#descricao").val(queixas_atuais);

    

 }


 // Código original (ultimo comentario) = https://pt.stackoverflow.com/questions/358308/passar-dados-para-uma-janela-modal-bootstrap