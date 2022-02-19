var script = document.createElement("script");
script.src = "https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js";
script.type = "text/javascript";
document.getElementsByTagName("head")[0].appendChild(script);

function replaceLinks() {
  $.each(
    $(".block-grid-item__component.image.image--link"),
    function (index, value) {
      var request = new XMLHttpRequest();
      request.open(
        "GET",
        "https://cdn.jsdelivr.net/gh/psychonout/arMonika@master/" + index
      );
      request.onload = function () {
        if (request.readyState === 4 && request.status === 200) {
          value.href = request.responseText;
        }
      };
      request.send(null);
    }
  );
}

$(window).on("load", replaceLinks());
