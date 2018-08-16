$(function(){
  $('div.main').fadeIn(800);
  $('div.images').css('background', 'rgba(0, 0, 0, 0.5)');
  $('ul li.list').css('display', 'none');
  $('ul li.list_after').fadeIn(800);
  $('img.batu').fadeIn(800);
});

$(function(){
  $('img.batu').on({'mouseenter' : function(){
    $(this).css('transform', 'scale(1.2)');
    $(this).css('box-shadow', '0 0 8px white');
  }, 'mouseleave' : function(){
    $(this).css('transform', 'scale(1.0)');
    $(this).css('box-shadow', 'none');
  }
 })
});

$(function(){
  $('img.batu').on('click', function(){
    $('div.images').fadeOut(800);
    $('ul li.list_after').fadeOut(800);
    $('img.batu').fadeOut(800);
    $('div.main').fadeOut(800);
  });
});
