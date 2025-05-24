document.addEventListener("DOMContentLoaded", async function () {
  const domainH = document.querySelector(".site-name");
  let url = "";

  const box = document.querySelector(".box");
  const reportbox = document.querySelector(".report-box");
  const reportButton = document.querySelector(".report-link");
  const sendReportButton = document.querySelector(".send-report");
  const formdata = document.querySelector(".form-data");
  const mal1 = document.getElementById("mal1");
  const mal2 = document.getElementById("mal2");
  const mal3 = document.getElementById("mal3");
  const mal4 = document.getElementById("mal4");
  const mal5 = document.getElementById("mal5");

  formdata.addEventListener("submit", (e) => {
    alert(JSON.stringify(e.target.elements));
  });

  reportButton.addEventListener("click", () => {
    box.style.display = "none";
    reportbox.style.display = "flex";
    reportButton.style.display = "none";
    sendReportButton.style.display = "block";
  });
  sendReportButton.addEventListener("click", () => {
    box.style.display = "flex";
    reportbox.style.display = "none";
    reportButton.style.display = "block";
    sendReportButton.style.display = "none";
    let arr = [];
    if (mal1.checked) {
      arr.push(mal1.value);
    }
    if (mal2.checked) {
      arr.push(mal2.value);
    }
    if (mal3.checked) {
      arr.push(mal3.value);
    }
    if (mal4.checked) {
      arr.push(mal4.value);
    }
    if (mal5.checked) {
      arr.push(mal5.value);
    }

    sendReportData(arr);
  });

  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    var activeTab = tabs[0];
    var tabUrl = new URL(activeTab.url);
    // alert(tabUrl + "    " + tabUrl.hostname);
    makerequest(tabUrl.href);
    domainH.innerHTML = tabUrl.hostname;
  });
});
let htmldata = "";

async function sendReportData(data) {
  // yaha likhna h send report wala url niche
  const res = await fetch("http://127.0.0.1:8000", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  const resdata = await res.json();
  console.log(resdata);
  changes(resdata)
}
async function makerequest(url) {
  const data = await fetch("http://127.0.0.1:5000", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      url,
    }),
  });
  console.log("done");
  const res = await data.json();
  changes(res)
}


async function changes(res){

  const score = document.querySelector(".score");
  const report = document.querySelector(".report-data");
  const maincon = document.querySelector(".main-con");
  const loader = document.querySelector(".loader");
  const noofpattern = document.querySelector(".noofpattern");
  const progress = document.querySelector(".progress");
  if (res) {
    loader.style.display = "none";
    maincon.style.display = "flex";
  }
  score.innerHTML = res.score;
  progress.style.width = "" + res.score + "%";
  noofpattern.innerHTML = res.Darkpatterns;
  report.innerHTML = "";
  res.list.map((item) => {
    report.innerHTML += `<li style="font-size: large"> <label class="c" for="r">${item}</label></li>`;
  });
  // alert(JSON.stringify(res));
  highlightStrings(res.marking);

}

function highlightStrings(stringsToHighlight) {
  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    chrome.scripting.executeScript({
      target: { tabId: tabs[0].id },
      func: (StringsToHighlight) => {
        // Function to escape special characters in a string

        // Loop through the strings to highlight
        StringsToHighlight.forEach(function (string) {
          console.log(string);
          string.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
          var regex = new RegExp(string, "gi");
          document.body.innerHTML = document.body.innerHTML.replace(
            regex,
            function (match) {
              return (
                '<span style="background-color: yellow;">' + match + "</span>"
              );
            }
          );
        });
      },
      args: [stringsToHighlight],
    });
  });
}
