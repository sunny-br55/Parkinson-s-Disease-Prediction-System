function scrollToPredict() {
  document.getElementById("predict").scrollIntoView({behavior:"smooth"});
}

function predict() {
  let inputs = document.querySelectorAll("input");
  let features = [];

  inputs.forEach(i => features.push(parseFloat(i.value)));

  fetch("/predict", {
    method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({features:features})
  })
  .then(res=>res.json())
  .then(data=>{
    let resultBox = document.getElementById("result");
    resultBox.innerText = data.result;
    resultBox.style.animation = "fadeIn 1s";
  });
}
