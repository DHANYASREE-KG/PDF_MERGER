const fileInput = document.getElementById("fileInput");
const addBtn = document.querySelector(".add-btn");
const fileList = document.getElementById("fileList");
const fileCount = document.getElementById("fileCount");
const mergeForm = document.getElementById("mergeForm");

let selectedFiles = [];

addBtn.addEventListener("click", () => {
    fileInput.click();
});

fileInput.addEventListener("change", (event) => {
    const files = Array.from(event.target.files);
    files.forEach(file => selectedFiles.push(file));
    updateFileList();
    fileInput.value = "";
});

function updateFileList() {
    fileList.innerHTML = "";

    selectedFiles.forEach((file, index) => {
        const li = document.createElement("li");
        li.innerHTML = `
            <span>${file.name}</span>
            <button type="button" class="remove-btn" onclick="removeFile(${index})">✖</button>
        `;
        fileList.appendChild(li);
    });

    fileCount.textContent = selectedFiles.length;
}

function removeFile(index) {
    selectedFiles.splice(index, 1);
    updateFileList();
}

mergeForm.addEventListener("submit", function () {
    const dataTransfer = new DataTransfer();
    selectedFiles.forEach(file => {
        dataTransfer.items.add(file);
    });
    fileInput.files = dataTransfer.files;
});

function closeModal() {
    document.querySelector(".modal-overlay").style.display = "none";
}