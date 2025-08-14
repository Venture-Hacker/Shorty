function copyText(txt) {
  navigator.clipboard.writeText(txt).then(() => {
    alert("Copied!");
  });
}
