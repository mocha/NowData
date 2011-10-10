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


  $('a.options_toggle.options_hidden').click(function(event){
    event.preventDefault();
    $(this).prev().dequeue().slideDown();
    $(this).text("Hide These Options");
    $(this).addClass("options_shown");
    $(this).removeClass("options_hidden");
    return false;
  });
  
  
  $('a.options_toggle.options_shown').click(function(event){
    event.preventDefault();
    $(this).prev().dequeue().slideUp();
    $(this).text("Show More Options");
    $(this).addClass("options_hidden");
    $(this).removeClass("options_shown");
    return false;
  });



});



