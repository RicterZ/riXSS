/**
 * Created by Ricter on 14-2-14.
 */



$(".project-edit").click(function(){
    //Set the views of the modal.
    $('#edit-project-name')[0].value = this.attributes['data-pro-name'].nodeValue;
    $('#edit-project-type').val(this.attributes['data-pro-type'].nodeValue);
    $('#edit-project-submit')[0].setAttribute("data-type", this.attributes['data-pro-id'].nodeValue);
    $('#editProject').modal('show');
})

$("#edit-project-submit").click(function(){
    var projectId = this.attributes['data-type'].nodeValue;
    $.ajax({
        type: 'PUT',
        url: '/projects/'+projectId+'/edit',
        dataType: 'json',
        data: {name: $('#edit-project-name').val(), type: $('#edit-project-type').val()},
        success: function() {
            $('#editProject').modal('hide');
            window.location.reload();
        },
        error: function(){
            alert('Modify Failed!');
        }
    })
})

$(".edit-module").click(function() {
    var module_id = this.attributes['data-type'].nodeValue;
    $("#edit-module-save").attr('data-type', module_id);
    $.ajax({
        type: 'GET',
        url: '/modules/' + module_id,
        dataType: 'json',
        success: function(data) {
            $("#edit-module-name")[0].value = data.name;
            $("#edit-module-script").val(data.script);
            $("#editModule").modal('show');
        }
    })
})


$("#edit-module-save").click(function() {
    var module_id = this.attributes['data-type'].nodeValue;
    $.ajax({
        type: 'PUT',
        url: '/modules/' + module_id,
        data: {name: $("#edit-module-name").val(), script: $("#edit-module-script").val()},
        dataType: 'json',
        success: function(data) {
            $("#editModule").modal('hide');
            window.location.reload();
        }
    })
})