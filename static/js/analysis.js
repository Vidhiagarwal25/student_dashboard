// Get the button that opens the popup
var graduationYearButton = document.getElementById("graduation-year-button");
// Get the popup
var graduationYearPopup = document.getElementById("graduation-year-popup");
// Get the <span> element that closes the popup
var closePopup = document.getElementsByClassName("close")[0];

// Function to show the popup
function showGraduationYearPopup() {
    graduationYearPopup.style.display = "block";
    // Send a request to the server to get the graduation year distribution
    fetch('/analysis')
        .then(response => response.json())
        .then(data => {
            // Update the table with the received data
            updateGraduationYearTable(data.graduation_year);
        })
        .catch(error => console.error('Error:', error));
}

// Function to hide the popup
function hideGraduationYearPopup() {
    graduationYearPopup.style.display = "none";
}

// Function to update the table with graduation year distribution
function updateGraduationYearTable(graduationYearData) {
    var tableBody = document.getElementById("graduation-year-table-body");
    // Clear existing content
    tableBody.innerHTML = '';
    // Add new rows
    Object.keys(graduationYearData).forEach(year => {
        var row = `<tr>
                        <td>${year}</td>
                        <td>${graduationYearData[year]}</td>
                  </tr>`;
        tableBody.innerHTML += row;
    });
}