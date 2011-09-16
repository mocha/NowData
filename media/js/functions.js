$(document).ready(function(){

  $('#right .browse_by_topic ul.topiclist.more').hide();

  $('#right .browse_by_topic a.reveal').click(function(event){
    event.preventDefault();
    $('#right .browse_by_topic ul.topiclist.more').dequeue().slideToggle();
    return false;
  });


  // $('#right .browse_by_topic').hide();


});
