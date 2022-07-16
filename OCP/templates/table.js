
$(".btn-insert-data").click(function(){
    var json_data=[];
     $(".input_data").each(function(){
     var value=$(this).val();
     var parent_html=$(this).parent();
     parent_html.html(value);
     $(this).remove();
     });
     $("tbody tr").each(function(){
     var id=$(this).children().eq(0).text()
     var First_Name=$(this).children().eq(1).text()
     var Last_Name=$(this).children().eq(2).text()
     var City=$(this).children().eq(3).text()
     var single_data={"id":id,"First_Name":First_Name,"Last_Name":Last_Name,"City":City};
     json_data.push(single_data);
     });
     var string_data=JSON.stringify(json_data)
     $.ajax({
     url:"{% url 'insert' %}",
     type:'POST',
     data:{data:string_data}
     })
     .done(function(response){
     if(response['error']==false){
     $("#upt_error").hide();
     $("#upt_success").text(response['errorMessage']);
     $("#upt_success").show();
    }
     else{
     $("#upt_success").hide();
     $("#upt_error").text(response['errorMessage']);
     $("#upt_error").show();
     }
     })
     .fail(function(){
     $("#upt_success").hide();
     $("#upt_error").text("Something Went Wrong!");
     $("#upt_error").show();
     })
    });