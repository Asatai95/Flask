$(function(){
  $('div.main').fadeIn(1200);
  $('div.image .header_text').fadeIn(1200);
});


$(function(){
  $('ul li.list').on({'mouseenter' : function(){
    $(this).find('p.title').css('opacity', '1');
    $(this).find('p.comment').css('opacity', '1');
    $(this).find('img').css('opacity', '0.5');
    $(this).css('transform', 'scale(1.1)');
    $(this).find('img').css('box-shadow', '0 0 8px white')

  }, 'mouseleave' : function(){
    $(this).find('p.title').css('opacity', '0');
    $(this).find('p.comment').css('opacity', '0');
    $(this).find('img').css('opacity', '1');
    $(this).css('transform', 'scale(1.0)');
    $(this).find('img').css('box-shadow', 'none')
  }
 })
});

// $(function(){
//   $('ul li.list').on('click', function(){
//     $('div.images').css('background', 'rgba(0, 0, 0, 0.5)');
//     $('ul li.list').css('display', 'none');
//     $('ul li.list_after').fadeIn(800);
//     $('img.batu').fadeIn(800);
//   });
// });
