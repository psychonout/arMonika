function replaceLinks() {
  const urls = document.getElementsByClassName(
    "block-grid-item__component image image--link"
  );
  for (let i = 0; i < urls.length; i++) {
    let element = urls[i];
    var request = new XMLHttpRequest();
    request.open("GET", "https://zwww.vystymaskitaip.lt/" + i);
    request.onload = function () {
      if (request.readyState === 4 && request.status === 200) {
        element.href = request.responseText;
      }
    };
  }
}
document.addEventListener("DOMContentLoaded", function (event) {
  replaceLinks();
});
