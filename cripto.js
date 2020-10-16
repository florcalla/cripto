// ==UserScript==
// @name         cripto
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       Flxr
// @require       https://cdnjs.cloudflare.com/ajax/libs/aes-js/3.1.2/index.min.js
// @match       https://florcalla.github.io/cripto/
// @grant        none
// ==/UserScript==


//VECTOR inicial iv es necesario en hexadecimal de 32 digitos de largo
var iv = document.getElementsByClassName('iv')[0].id;
var iv_bytes = aesjs.utils.hex.toBytes(iv);
//LLAVE DE 32 DIGITOS key es necesario en hexadecimal de 32 digitos de largo

var key ='58a53a92e90ca0e97fc5754ae5189f79';
var key_bytes = aesjs.utils.hex.toBytes(key);

// Convertir texto en bytes


var text = document.getElementsByClassName('AES')[0].id;
console.log(text)

//desencriptar
var encryptedBytes = aesjs.utils.hex.toBytes(text);
var aesOfb = new aesjs.ModeOfOperation.ofb(key_bytes, iv_bytes);
var decryptedBytes = aesOfb.decrypt(encryptedBytes);
var decryptedText = aesjs.utils.utf8.fromBytes(decryptedBytes);
console.log(decryptedText)

//mostrar en pantalla

document.getElementById(text).innerHTML=decryptedText;
