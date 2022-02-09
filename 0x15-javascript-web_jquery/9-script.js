const url = "https://fourtonfish.com/hellosalut/?lang=fr";
$.getJSON(url, function(result){
    $("DIV#hello").append(result.hello);
});
