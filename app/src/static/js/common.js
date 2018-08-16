// $(function(){
//   $('div.text_buttom').on('click', function(){
//     $('div.text_buttom').css('opacity', '0');
//     $('div.text_buttom').css('z-index', '5');
//     $('div.ma_text form').css('opacity', '1');
//     $('div.ma_text input').css('z-index', '10');
//     $('button.submit').css('z-index', '10');
//     $('div.ma_text input').css('width', '450px');
//   });
// });

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

$(function(){
  $('header').fadeIn(800, function(){
    $(this).prop('used', true);
  });
  $('div.machine').fadeIn(1800, function(){
    $(this).prop('used', true);
  });
  $('div.community').fadeIn(1800, function(){
    $(this).prop('used', true);
  });
});


$(function(){
  $('div.text_buttom').on('click', function(){
    $('div.machine').fadeOut('slow');
    $('div.machine').css('z-index', '10');
    $('div.content').css('z-index', '15');
    $('div.content').fadeIn('slow');
    $('div.community').css('bottom', '30px');
  });
});

// $(function(){
//   $('button.search').click(function(e){
// 	  e.preventDefault();
//   });
// });
