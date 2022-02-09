const $ = window.$;
$(window).bind('load', function () {
  $('INPUT#btn_translate').click(function () {
    const code = $('INPUT#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/?lang=${code}`;
    $.getJSON(url, function (result) {
      $('DIV#hello').replaceWith(`<div id='hello'>${result.hello}</div>`);
    });
  });
});
