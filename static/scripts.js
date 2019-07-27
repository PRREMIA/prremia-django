function SeeMore() {
    var moreText = document.getElementById("more");
    var btnText = document.getElementById("seemore");

    if (moreText.style.display === "inline") {
        btnText.innerHTML = "See more";
        moreText.style.display = "none";
    } else {
        btnText.innerHTML = "See less";
        moreText.style.display = "inline";
    }
}