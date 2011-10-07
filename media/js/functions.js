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
  
  
  $('a.options_toggle').click(function(event){
    event.preventDefault();
    $(this).prev().dequeue().slideToggle();
    return false;
  });

  // $('#right .browse_by_topic').hide();


});
