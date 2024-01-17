document.addEventListener("DOMContentLoaded", function () {
    const filterInput = document.getElementById("filterInput");
    const resultList = document.getElementById("resultList");

    filterInput.addEventListener("input", function () {
        const inputValue = filterInput.value.toLowerCase();
        filterResults(inputValue);
    });

    function filterResults(query) {
        // Assuming mock data
        const mockData = [
            { id: 1, name: "Item 1" },
            { id: 2, name: "Item 2" },
            { id: 3, name: "Item 3" },
            // Add more data as needed
        ];

        const filteredData = mockData.filter(item => item.name.toLowerCase().includes(query));

        displayResults(filteredData);
    }

    function displayResults(results) {
        resultList.innerHTML = "";
        results.forEach(result => {
            const listItem = document.createElement("li");
            listItem.textContent = result.name;
            resultList.appendChild(listItem);
        });
    }
});
