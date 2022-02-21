function replaceLinks() {
  const urls = document.getElementsByClassName(
    "block-grid-item__component image image--link"
  );
  for (let i = 0; i < urls.length; i++) {
    let element = urls[i];
    let request = new XMLHttpRequest();
    let url = "https://www.vystymaskitaip.lt/" + i;
    request.open("GET", url);
    request.onload = function () {
      if (request.readyState === 4 && request.status === 200) {
        element.href = request.responseText;
      }
    };
    request.send();
  }
}
console.log("Replacing links");
setTimeout(replaceLinks(), 100);
