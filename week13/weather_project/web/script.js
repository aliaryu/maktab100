const div_response = document.querySelector(".response")

document.getElementById("form").addEventListener("submit", function(event) {
    event.preventDefault(); // dont refresh page
  
    var city = document.getElementById("input-city").value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        console.log(response);

        while (div_response.firstChild) {
            div_response.removeChild(div_response.firstChild);
          }
        div_response.classList.add("on")
        var p1 = document.createElement("p");
        var p2 = document.createElement("p");
        var p3 = document.createElement("p");
        p1.textContent = "temperature:" + " " + response.temperature
        p2.textContent = "feels like:"  + " " + response.feels_like
        p3.textContent = "last update:" + " " + response.last_updated

        div_response.appendChild(p1)
        div_response.appendChild(p2)
        div_response.appendChild(p3)
      } else {
        while (div_response.firstChild) {
            div_response.removeChild(div_response.firstChild);
          }
        div_response.classList.add("on")
        var p1 = document.createElement("p");
        p1.textContent = "unexpected error. city not found or web is down."
        div_response.appendChild(p1)
      }
    };
    xhr.send("city_name=" + encodeURIComponent(city));
  });
