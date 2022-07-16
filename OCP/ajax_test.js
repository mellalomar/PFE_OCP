$(function(){   
    var myCell = document.getElementById("desc");
    var cellContents = (myCell.innerHTML);
     $('.clicks').click(function() {             
         $.ajax({     
             type: "POST",   
             url: "/myapp/test_ajax/", 
             data: {   
                 'ajax_data' : cellContents, 
                 'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val() 
             },
             success: ajaxSuccess, 
             dataType: 'html'
         });
 
     });
 
 });
 
 function ajaxSuccess(data, textStatus, jqXHR) 
 {
     $('.here').html(data); //I would like to put this in the "click to show" cell. I was placing it in a random div for testing.
 }