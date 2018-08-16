$(function(){
  $('div.search_top textarea').bind('keydown keyup keypress change',function(){
    var count = $('div.search_top textarea').val().length;

    if (count <= 29 && count >= 1) {
      $('div.search_top textarea').bind('keydown keyup keypress change',function(){
          var thisValueLength = $(this).val().length + '/30';
          $('p.count').html(thisValueLength);
      });
    } else if (count == 30) {
      $('div.search_top textarea').bind('keydown keyup keypress change',function(){
          var thisValueLength = '30/30';
          var text = 'OK!'
          $('p.count').text(text);
      });
    } else if (count == 0) {
        $('div.search_top textarea').bind('keydown keyup keypress change',function(){
            var thisValueLength ='0/30';
            $('p.count').html(thisValueLength);
        });
    }
  });
});
