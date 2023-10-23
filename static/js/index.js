$(function(){
    var loadForm = function(){
        let btn = $(this); //Seleciona o elemento onde a função foi executada
        $.ajax({
            url: btn.attr("data-url"), // Busca o conteúdo do data do elemento
            type: 'get', // Tipo de requisição
            dataType: 'json', 
            beforeSend: function(){ // Antes de enviar o conteúdo, ou seja, enviar o formulário em questão 
                $('#modal').modal("show");
            },
            success: function(data){ // Quando a ação de enviar é bem sucedida
                $("#modal .modal-content").html(data.html_form);
            },
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
                    $(".campo").html(data.html_list)
                    $("#modal").modal("hide");
                }
                else{
                    $("#modal .modal-content").html(data.html_form);
                }
            }
        });
        return false
    };

    var mudarUrl = function(){
        let btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',

            success: function(){
                window.location.replace(btn.attr("data-url"))
            }
        });
    };

    // NAVEGAR NAS PÁGINAS PELOS BOTÕES
    $(".section-informacoes").on("click", ".botao", mudarUrl);

    // ########## EXCLUIR ##########
    $(".campo").on("click", "#js-delete", loadForm);
    $("#modal").on("submit", "#js-delete-form", saveForm);

    // ########## EDITAR ##########
    $(".campo").on("click", "#js-update", mudarUrl);

});