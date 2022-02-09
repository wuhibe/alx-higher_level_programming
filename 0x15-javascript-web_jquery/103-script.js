const $ = window.$;
$(window).bind('load', function () {
  $('INPUT#btn_translate').click(function () {
    const code = $('INPUT#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/?lang=${code}`;
    $.getJSON(url, function (result) {
      $('DIV#hello').replaceWith(`<div id='hello'>${result.hello}</div>`);
    });
  });
  $('INPUT#language_code').keydown(function (event) {
    const keyCode = (event.keyCode ? event.keyCode : event.which);
    if (keyCode === 13) {
      $('INPUT#btn_translate').trigger('click');
    }
  });
});
