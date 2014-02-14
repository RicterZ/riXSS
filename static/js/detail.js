/**
 * Created by Ricter on 14-2-14.
 */
$(".view").click(function (){
    var parentObj = $(this).parent();
    $(".result-server-data").html($(parentObj[0]).children(".server-data").html());
    $(".result-cookie").html($(parentObj[0]).children(".cookies").html());
    $("#projectResult").modal('show');
})