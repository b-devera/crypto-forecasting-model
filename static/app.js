var btc = document.getElementById("bitcoin");
var eth = document.getElementById("ethereum");
var usdt = document.getElementById("tether");
var bnb = document.getElementById("binancecoin");
var xrp = document.getElementById("ripple");
var ada = document.getElementById("cardano");
var sol = document.getElementById("solana");
var dot = document.getElementById("polkadot");
var doge = document.getElementById("dogecoin");
var dai = document.getElementById("dai");

var price = {
    "async": true,
    "scroosDomain": true,
    "url": "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Ctether%2Cbinancecoin%2Cripple%2Ccardano%2Csolana%2Cpolkadot%2Cdogecoin%2Cdai&vs_currencies=usd",

    "method": "GET",
    "headers": {}
}

$.ajax(price).done(function (response) {
    btc.innerHTML = response.bitcoin.usd;
    eth.innerHTML = response.ethereum.usd;
    usdt.innerHTML = response.tether.usd;
    bnb.innerHTML = response.binancecoin.usd;
    xrp.innerHTML = response.ripple.usd;
    ada.innerHTML = response.cardano.usd;
    sol.innerHTML = response.solana.usd;
    dot.innerHTML = response.polkadot.usd;
    doge.innerHTML = response.dogecoin.usd;
    dai.innerHTML = response.dai.usd;
})