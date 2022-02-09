$('DIV#toggle_header').click(function () {
  $('header').toggleClass('red');
  if ($('header.red')) {
    $('header').toggleClass('green');
  } else {
    $('header').toggleClass('red');
  }
});
