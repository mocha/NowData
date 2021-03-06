
function clearForm(oForm) {
   
  var elements = oForm.elements;
   
  oForm.reset();

  for(i=0; i<elements.length; i++) {
     
  field_type = elements[i].type.toLowerCase();
 
  switch(field_type) {
 
    case "text":
    case "password":
    case "textarea":
          case "hidden":  
     
      elements[i].value = "";
      break;
       
    case "radio":
    case "checkbox":
        if (elements[i].checked) {
          elements[i].checked = false;
      }
      break;

    case "select-one":
    case "select-multi":
                elements[i].selectedIndex = -1;
      break;

    default:
      break;
  }
    }
}


$(document).ready(function(){


  $('#right .browse_by_topic ul.topiclist.more').hide();


  $('#right .browse_by_topic a.reveal').click(function(event){
    event.preventDefault();
    $('#right .browse_by_topic ul.topiclist.more').dequeue().slideToggle();
    return false;
  });



  $('a.toggle_resources').click(function(event){
    event.preventDefault();
    $(this).next().dequeue().slideToggle();
    return false;
  });


  // $('a.options_toggle').click(function(event){
  //   event.preventDefault();
  //   $(this).prev().dequeue().slideToggle();
  //   return false;
  // });


  $('a.options_toggle.options_hidden').live('click', function(event){
    event.preventDefault();
    $(this).prev().dequeue().slideDown();
    $(this).text("Hide These Options");
    $(this).addClass("options_shown");
    $(this).removeClass("options_hidden");
    return false;
  });
  
  
  $('a.options_toggle.options_shown').live('click', function(event){
    event.preventDefault();
    $(this).prev().dequeue().slideUp();
    $(this).text("Show More Options");
    $(this).addClass("options_hidden");
    $(this).removeClass("options_shown");
    return false;
  });


});



