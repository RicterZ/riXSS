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