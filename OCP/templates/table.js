
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
     var name=$(this).children().eq(1).text()
     var BPL=$(this).children().eq(2).text()
     var MgO=$(this).children().eq(3).text()
     var MO=$(this).children().eq(4).text()
     var SiO2=$(this).children().eq(5).text()
     var CO2=$(this).children().eq(6).text()
     var distance=$(this).children().eq(7).text()
     var single_data={"id":id,"name":name,"BPL":BPL,"MgO":MgO,"MO":MO,"SiO2":SiO2,"CO2":CO2,"distance":distance};
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