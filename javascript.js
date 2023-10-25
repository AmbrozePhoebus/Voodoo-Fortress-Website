var button = document.createElement("button");
button.innerHTML = "Click me";

button.onclick = function () {
    alert("Button clicked");
};

document.body.appendChild(button);