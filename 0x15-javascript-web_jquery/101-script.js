const $ = window.$;
$(window).bind('load', function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });

  $('DIV#remove_item').click(function () {
    $('.my_list li').first().remove();
  });

  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
