$(function(){
  $('p.red a').on('click', function(){
    $(this).text('変更済み');
    $(this).css('color', 'blue')
  });
});
