$(function(){
    var loadForm = function(){
        let btn = $(this); //Seleciona o elemento onde a função foi executada
        $.ajax({
            url: btn.attr("data-url"), // Busca o conteúdo do data do elemento
            type: 'get', // Tipo de requisição
            dataType: 'json', 
            beforeSend: function(){ // Antes de enviar o conteúdo, ou seja, enviar o formulário em questão 
                $('#modal-post').modal("show");
            },
            success: function(data){ // Quando a ação de enviar é bem sucedida
                $("#modal-post .modal-content").html(data.html_form);
            },
            error: function(result){
                alert("Erro")
            }
        });
    };

    var saveForm = function(){
        let form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function(data){
                if(data.form_is_valid){
                    $("#modal-post").modal("hide");
                }
                else{
                    $("#modal-post .modal-content").html(data.html_form);
                }
            }
        });
        return false
    };

   
    // ########## EXCLUIR PIZZA ##########
    $(".postagem").on("click", ".js-delete", loadForm);
    $("#modal-post").on("submit", "#js-delete-form", saveForm);
});