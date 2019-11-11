window.addEventListener("load", function() {
  function hideLoad() {
    const loader = this.document.querySelector(".loader");
    loader.classList.add("hide");
  }

  setTimeout(hideLoad, 300);
});

function get(object) {
  return $.getJSON(object.url, object.callback);
}

function getCardImg(account) {
  if (account.account_type == "W") {
    return "money.png";
  } else if (account.bank_name == "NU") {
    return "nuCard.png";
  } else if (account.bank_name == "SA") {
    return "santanderCard.png";
  }
}
