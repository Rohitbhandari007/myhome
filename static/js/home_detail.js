const homeID = document.getElementById("home-id").value;
const url = "ws://" + window.location.host + "/ws/home/" + homeID + "/";
const socket = new WebSocket(url);

socket.onopen = (event) => {
  console.log("WebSocket connection opened:", event);
};

socket.onclose = (event) => {
  console.log("WebSocket connection closed:", event);
};

socket.onmessage = (event) => {
  const data = JSON.parse(event.data);
  updateLights(data);
  console.log("WebSocket message received:", data);
};

/**
 * Sends a message through the socket.
 * @param {Object} message - The message to be sent.
 */
function sendMessage(message) {
  socket.send(JSON.stringify(message));
}

/**
 * Handles the apply button click event.
 *
 * @param {HTMLElement} btn - The apply button element.
 */
function handleApply(btn) {
  const lightId = btn.dataset.lightId;
  const message = prepareMessage(lightId);
  sendMessage(message);
}

function handleSave(btn) {
  const lightId = btn.dataset.lightId;
  const message = prepareMessage(lightId, true);
  sendMessage(message);
}

/**
 * Prepares a message object with the specified light ID, brightness, color, and switch state.
 * @param {string} lightId - The ID of the light.
 * @param {boolean} save - Whether the message is for saving the light state to the database.
 * @returns {object} - The prepared message object.
 */
function prepareMessage(lightId, save = false) {
  const lightElem = document.getElementById(`light-${lightId}`);

  const brightness = lightElem.querySelector(".light-brightness").value;
  const color = lightElem.querySelector(".light-color").value;
  const lightSwitch = lightElem.querySelector(".light-switch").checked;
  let currentSwitch = "off";
  if (lightSwitch === true) {
    currentSwitch = "on";
  } else {
    currentSwitch = "off";
  }
  let data = {
    light_id: lightId || null,
    switch: currentSwitch,
    brightness: brightness || null,
    color: color || null,
    save: save,
  };
  console.log(data);
  return data;
}

/**
 * Updates the lights based on the provided data.
 * @param {Object} data - The data containing the light information.
 * @param {string} data.light_id - The ID of the light element.
 * @param {string} data.color - The color of the light.
 * @param {number} data.brightness - The brightness of the light (0-100).
 * @param {string} data.switch - The switch state of the light.
 */
function updateLights(data) {
  const lightElem = document.getElementById(`light-${data.light_id}`);
  const lightBox = lightElem.querySelector(".light-box");
  lightBox.style.backgroundColor = data.color;

  lightElem.querySelector(".light-brightness").value = data.brightness;
  lightElem.querySelector(".light-color").value = data.color;
  lightElem.querySelector(".light-switch").checked = data.switch === "on" ? true : false;
  lightElem.querySelector(".light-status").querySelector(".status").innerText =
    "Status:" + data.switch;
  lightElem.querySelector(".brightness").innerHTML = data.brightness + "%";

  const bulb = lightElem
    .querySelector(".light-status")
    .querySelector(".light-image");
  if (data.switch === "off"){
    bulb.src = bulb.src.replace("bulb-on", "bulb-off");
  } else{
    bulb.src = bulb.src.replace("bulb-off", "bulb-on");
  }
}
